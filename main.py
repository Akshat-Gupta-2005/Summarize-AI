from transformers import pipeline

model = pipeline("summarization", model="facebook/bart-large-cnn")
# response = model("Your long text goes here", max_length=130, min_length=30, do_sample=False)

response = model("i love programming in python. it is a very versatile language. it can be used for web development, data science, machine learning, artificial intelligence, and more. python has a large community and a wealth of libraries and frameworks that make development easier and faster.", max_length=30)
print(response)