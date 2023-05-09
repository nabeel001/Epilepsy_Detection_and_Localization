from flask import Flask, request, render_template
from scipy.signal import butter, filtfilt
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

# Load the saved models
localisation_model = load_model('models/localisation_model.h5')
detection_model = load_model('models/detection_model.h5')

# Define the filter parameters
lowcut = 0.5
highcut = 85
fs = 173.61
order = 5

# Compute the Nyquist frequency
nyquist = 0.5 * fs

# Compute the filter cutoff frequencies as fractions of the Nyquist frequency
low = lowcut / nyquist
high = highcut / nyquist

# Compute the filter coefficients
b, a = butter(order, [low, high], btype='band')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detection', methods=['POST'])
def detection():

    # Get the uploaded file and read 
    file = request.files['file']

    # Read the file contents and convert to numpy array
    signal = np.loadtxt(file)
    signal = np.array(signal)

    # Plot the line chart
    plt.figure(figsize=(20,4))
    plt.axhline(0, color='grey')
    plt.plot(signal)
    plt.xlabel('Time')
    plt.ylabel('Intensity')
    plt.title('Input EEG Signal')
    plt.savefig('static/plots/signal_detection_plot.png')
    
    # Apply the filter to the data
    filtered_signal = filtfilt(b, a, signal)

    # Reshape the signal to match the input shape of the model
    filtered_signal = filtered_signal.reshape(1, filtered_signal.shape[0], 1)
    
    # Make the prediction
    prediction = detection_model.predict(filtered_signal)

    # Return the prediction as a string
    prediction_str = "SEIZURE DETECTED" if int(round(prediction[0][0])) == 1 else "NO SEIZURE DETECTED"

    return render_template('index.html', plot_detection='static/plots/signal_detection_plot.png', detection=prediction_str)


@app.route('/localisation', methods=['POST'])
def localisation():

    # Get the uploaded file
    file = request.files['file']

    # Read the file contents and convert to numpy array
    signal = np.loadtxt(file)
    signal = np.array(signal)

    # Plot the line chart
    plt.figure(figsize=(20,4))
    plt.axhline(0, color='grey')
    plt.plot(signal)
    plt.xlabel('Time')
    plt.ylabel('Intensity')
    plt.title('Input EEG Signal')
    plt.savefig('static/plots/signal_localisation_plot.png')

    # Apply the filter to the data
    filtered_signal = filtfilt(b, a, signal)

    # Reshape the signal to match the input shape of the model
    filtered_signal = filtered_signal.reshape(1, filtered_signal.shape[0], 1)
    
    # Make the prediction
    prediction = localisation_model.predict(filtered_signal)

    # Return the prediction as a string
    prediction_str = "FOCAL SIGNAL" if int(round(prediction[0][0])) == 0 else "NON-FOCAL SIGNAL"

    return render_template('index.html', plot_localisation='static/plots/signal_localisation_plot.png', localisation=prediction_str)
