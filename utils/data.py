# -*- coding: utf-8 -*-


import pandas as pd
from sklearn.metrics import accuracy_score, cohen_kappa_score, f1_score, confusion_matrix
from utils import config

def read_data(data_path, col_smiles='smiles', col_target='HIV_active'):
    
    # read data
    df = pd.read_csv(data_path, sep=',')
    df_no_na = df[[col_smiles, col_target]].dropna()

    X = df_no_na[col_smiles]
    y = df_no_na[col_target].values
    
    return X, y

                
def get_prediction_score(y_label, y_predict):
    
    scores = {}
    scores[config.METRIC_ACCURACY] = accuracy_score(y_label, y_predict)
    scores[config.METRIC_F1_SCORE] = f1_score(y_label, y_predict, labels=None, average='macro', sample_weight=None)
    scores[config.METRIC_COHEN_KAPPA] = cohen_kappa_score(y_label, y_predict)
    scores[config.METRIC_CONFUSION_MATRIX] = confusion_matrix(y_label, y_predict)
    
    return scores