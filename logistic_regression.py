# -*- coding: utf-8 -*-
"""Logistic regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rDvuQQ6OwW3FNxnzBpKmLuHpNGp0oA_u
"""

from google.colab import data_table
import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

data_table.enable_dataframe_formatter()

pa = pd.read_csv("/content/drive/MyDrive/Home Credit/application_test.csv")
from sklearn.model_selection import train_test_split
trainingSet, testSet = train_test_split(pa, test_size=0.2)
train_pa = trainingSet
test_pa = testSet
X_train = train_pa[["SK_ID_CURR","CNT_CHILDREN"]] 	
y_train = train_pa["CODE_GENDER"]
X_test = test_pa[["SK_ID_CURR","CNT_CHILDREN"]] 	
y_test = test_pa["CODE_GENDER"]
y_test.head()
y_train.value_counts()
sns.countplot("CODE_GENDER", data=train_pa, palette='Blues_d')
plt.show()
plt.savefig('count_plot')
count_male = len(train_pa[train_pa['CODE_GENDER']=="M"])
count_female = len(train_pa[train_pa['CODE_GENDER']=="F"])
pct_of_male = count_male/(count_male+count_female)
print("percentage of male is", pct_of_male*100)
pct_of_female = count_female/(count_male+count_female)
print("percentage of female is", pct_of_female*100)
train_pa.groupby('CODE_GENDER').mean()
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred = logreg.predict(X_test)
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
cnf_matrix
class_names=['F','M']
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix', y=1.1)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
display(pa)