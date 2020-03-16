# -*- coding: utf-8 -*-

##########################
## FOLDER STURCTURE ######
##########################
WORK_DIRECTORY = '/drug-efficacy/'
DATA_FILE = 'HIV.csv'

##########################
## EVALUATION METRICS ####
##########################
METRIC_ACCURACY = 'accuracy'
METRIC_F1_SCORE = 'f1-score'
METRIC_COHEN_KAPPA = 'Cohen kappa'
METRIC_CONFUSION_MATRIX = 'Confusion Matrix'

###############
## MODEL ######
###############
CLASSES = ['benign', 'malignant']
TEST_RATIO = 0.2
SEED = 0