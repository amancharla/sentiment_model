import sentiment_model as sentimentmodel

sample_text = "The Dow Jones Industrial Average (^DJI) turned green."

model = sentimentmodel.SentimentModel()
sentiment = model.predict(text=sample_text)
print(sentiment)

