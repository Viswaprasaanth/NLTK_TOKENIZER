# -*- coding: utf-8 -*-
"""WordCloud.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1daGlNqel8JUiwJfObNx6dmPsym0WgShx
"""

#Install the wordcloud library:
!pip install wordcloud

#Import libraries:
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

#Mount Google Drive:
from google.colab import drive
drive.mount('/content/drive')

#Load the text file:
with open("/content/drive/MyDrive/WORD CLOUD/JaneEyre.txt", "r") as file:
  text = file.read()

#Create a WordCloud object:
wordcloud = WordCloud(
width=800,
height=400,
background_color="white",
stopwords=set(STOPWORDS),
min_font_size=10,
).generate(text)

#Display the word cloud:
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

from matplotlib import cm
stopwords = set(STOPWORDS)
if "said" in stopwords:
  stopwords.remove("said")
#Create a WordCloud object:
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="Black", colormap=cm.viridis,
    stopwords=stopwords,
    max_words=100,
    min_font_size=10
).generate(text)
#Display the word cloud:
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()



from PIL import Image
import numpy as np

mask = np.array(Image.open("/content/drive/MyDrive/WORD CLOUD/output.png"))

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    stopwords=set(STOPWORDS),
    min_font_size=10,
    mask=mask # This line is added to use the mask
).generate(text)
#Display the word cloud:
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()