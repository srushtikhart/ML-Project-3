# -*- coding: utf-8 -*-
"""Day3 ML Project credit card fraud detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15bm7wf8A4nfhvku3jDl5qwn49vZbC1cI
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/credit.csv')

df.head()

df.info()

df.describe()

df=df.drop('ID', axis=1)

df.head()

df.isnull().sum()

cat_cols=['SEX','EDUCATION','MARRIAGE','PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']
fig,ax=plt.subplots(1,4,figsize=(25,5))
for cols,subplots in zip(cat_cols,ax.flatten()):
  sns.countplot(x=df[cols],ax=subplots)

yes = (((df['default.payment.next.month']==1).sum())/len(df['default.payment.next.month']))*100
no = (((df['default.payment.next.month']==0).sum())/len(df['default.payment.next.month']))*100
x=[yes,no]

plt.pie(x,labels=['yes','no'], colors=['red', 'blue'] , radius=2, autopct='%1.0f%%')
plt.title('default.payment.next.month')
plt.show()

df['default.payment.next.month'].value_counts(normalize=True)

from sklearn.model_selection import train_test_split

x=df.drop('default.payment.next.month',axis=1)
y=df['default.payment.next.month']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier()

model=rfc.fit(X_train,y_train)

prediction=model.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
print(classification_report(y_test,prediction))

