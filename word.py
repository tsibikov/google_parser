import io
from collections import Counter
from os import path

import matplotlib.pyplot as plt
from wordcloud import WordCloud

d = path.dirname(__file__)

# It is important to use io.open to correctly load the file as UTF-8
text = io.open(path.join(d, 'file.txt')).read()

words = text.split()
print(Counter(words))

# Generate a word cloud image
# The Symbola font includes most emoji
font_path = path.join(d, 'Symbola.ttf')
word_cloud = WordCloud(font_path=font_path).generate(text)

# Display the generated image:
plt.imshow(word_cloud)
plt.axis("off")
plt.show()