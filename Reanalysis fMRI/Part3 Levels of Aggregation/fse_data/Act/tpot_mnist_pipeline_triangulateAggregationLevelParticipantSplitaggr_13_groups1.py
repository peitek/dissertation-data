import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline, make_union
from sklearn.svm import LinearSVC
from tpot.builtins import StackingEstimator, ZeroCount

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:0.9204433497536947
exported_pipeline = make_pipeline(
    StackingEstimator(estimator=LinearSVC(C=0.5, dual=False, loss="squared_hinge", penalty="l2", tol=0.0001)),
    StackingEstimator(estimator=LinearSVC(C=0.0001, dual=True, loss="squared_hinge", penalty="l2", tol=0.01)),
    ZeroCount(),
    KNeighborsClassifier(n_neighbors=78, p=2, weights="distance")
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
