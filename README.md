# Epilepsy_Detection_and_Localization

Epilepsy is a long-term neurological condition that affects the brain. It is identified by the recurrence of abnormal electrical activities in the brain called seizures which is captured using Intracranial Electroencephalogram (iEEG) technique. It is a time consuming and error-prone process to detect seizure activity and to localize the seizure focus using visual subjective discrimination manually. In this project, the BONN Dataset is used for analysis. 

For detecting the seizure activity in the signal, a number of deep learning techniques like LSTM, GRU and 1D CNN have been trained and tested. Similarly for the purpose of localization the key features in the signal are extracted using an autoencoder whose output is then fed to various classification algorithms like KNN, adaptive gradient boosting, random forest, logistic regression, SVM, MLP and 1D CNN. In addition to the aforementioned workflow for the localization of iEEG signals, RNN based Transformer approach was implemented. 

## Overall Project Design:
![Overall Project Design](overall_system_design.png)

## Results:

<ins>**Epilepsy Detection:**</ins>

| Model                                   | Accuracy|
| --------------------------------------- | ------- |
| 1D Convolutional Neural Network (CNN)   | 92.50%  |
| Gated Recurrent Unit (GRU)              | 93.75%  |
| **Long Short-Term Memory (LSTM)**       | **94.99%**  |

<ins>**Epilepsy Localization:**</ins>

| Model                                     | Accuracy   |
|-------------------------------------------|------------|
| Logistic Regression                       | 77.50%     |
| k-Nearest Neighbours (KNN)                | 72.50%     |
| Support Vector Machine (SVM)              | 75.00%     |
| Ensemble Model using Random Forest        | 77.50%     |
| Ensemble Model using AdaBoost             | 75.00%     |
| Multi-Layer Perceptron (MLP)              | 82.50%     |
| RNN Based Transformer                     | 75.00%     |
| **1D Convolutional Neural Network (CNN)** | **87.50%** |

## Web Application - Screenshots:
