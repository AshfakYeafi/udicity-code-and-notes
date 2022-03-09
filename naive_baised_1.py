import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df=pd.read_csv("emai.csv")



# X = data.iloc[:,1:3001]
# Y = data.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(df["Message"],df["Category"],test_size=0.2)
# model=MultinomialNB()
# model.fit(X_train,y_train)
# y_pred=model.predict(X_test)
# print(accuracy_score(y_test,y_pred))
# v = CountVectorizer()
emails = [
    "Hey mohan, can we get together to watch footbal game tomorrow?",
    "Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!"
]
# v.fit_transform(X_test)

# emails_count = v.transform(emails)
# model.predict(emails_count)