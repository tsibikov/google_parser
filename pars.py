import requests
from bs4 import BeautifulSoup
from datetime import datetime
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud



def get_html(url):
    result = requests.get(url)
    return result.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h3 = soup.findAll('h3')
    t = soup.findAll('time')
    date_list = []
    header_list = []
    for time in t:
        temp_time = time['datetime']
        date_object = datetime.strptime(temp_time, '%Y-%m-%dT%H:%M:%Sz')
        date_list.append(date_object)
    for header in h3:
        header_list.append(header.text)
        print(header.text)
    result = []
    n = 0
    for i in range(len(header_list)):
        if date_list[i] > datetime.strptime('2020-10-05', '%Y-%m-%d'):
            if n < 50:
                result.append(header_list[i])
                n += 1
    myString = ' '.join(result)            
    word_cloud(myString)

def word_cloud(myString):
    d = path.dirname(__file__)
    font_path = path.join(d, 'Symbola.ttf')   
    word_cloud = WordCloud(font_path=font_path).generate(myString)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()

def main():
    url = 'https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFppYm5vU0FtVnVLQUFQAQ?hl=en-US&gl=US&ceid=US%3Aen'
    html = get_html(url)
    get_data(html)

if __name__ == "__main__":
    main()