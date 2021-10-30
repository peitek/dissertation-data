import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

# NOTE: Make sure that the class is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1).values
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'].values, random_state=42)

# Score on the training set was:0.9333333333333333
exported_pipeline = GradientBoostingClassifier(learning_rate=0.001, max_depth=7, max_features=0.2, min_samples_leaf=3, min_samples_split=7, n_estimators=100, subsample=1.0)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)