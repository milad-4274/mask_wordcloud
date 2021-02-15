from os import path
# from PIL import Image
import cv2
import numpy as np
from persian_wordcloud.wordcloud import STOPWORDS, PersianWordCloud
import argparse


# parser = argparse.ArgumentParser(description='Process some integers.')

# parser.add_argument('integers', metavar='N', type=int, nargs='+',help='an integer for the accumulator')



# d = path.dirname(__file__)

# text = open(path.join(d, 'shahname.txt'), encoding='utf-8').read()

# Add another stopword
# twitter_mask = np.array(Image.open(path.join(d, "twitter.jpg")))
# STOPWORDS.add('شاهنامه')


# stop_words = ["and", "of", "have","to","of","the","that","this","Pg",
#               "with","for","from","or","in","it","as","but","it","is",
#               "has","be","we","is not","an","will","on",'one','which',
#               'all','its','he','are','such','every','been','they','their',
#               'itself','more','most','what','his','man','was','who',
#               'so','by','not','even','there','was','these','only','should',
#               'into','had','at','no','do','them','can','would','himself',
#               'first','than','other','whole','any','when','our','against',
#               'must','those','being','themselves','also','very','you','just',
#               'men','much','him','much','thing','does','own','new','my','us',
#               'without','self','some','may','over','once','out','come','how',
#               'were','make','too','kind','tm','too','like','if','up','good',
#               'form','great','really','case','still'] + list(STOPWORDS)

# stop_words = ['بود','چو','شاهنامه','شاه','لشکر'] + list(STOPWORDS)

# Generate a word cloud image

# wordcloud = PersianWordCloud(
#     only_persian=False,
#     max_words=1000,
#     stopwords=stop_words,
#     margin=0,
#     width=800,
#     height=800,
#     min_font_size=1,
#     max_font_size=500,
#     random_state=True,
#     background_color="white",
#     mask=twitter_mask
# ).generate(text)

# image = wordcloud.to_image()
# image.show()
# image.save('twitter_mask.png')
def read_file(txt_file):
    # print(txt_file)
    text = open( txt_file, encoding='utf-8').read()
    return text

def read_img(img_file):
    img = cv2.imread(img_file)
    return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def read_words(txt_file):
    txt = read_file(txt_file)
    return txt.split()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--txt', help='main text file',type=str, required=True)
    parser.add_argument('--mask', help='binary mask', type=str, required=True)
    parser.add_argument('--stopwords', help='words you don\'t want',type=str, required=False)
    parser.add_argument('--startwords',help='stopwords that come first',type=str,required=False)
    parser.add_argument('--persian',help='language is persian?', type=bool, default=True)
    parser.add_argument('--maxwords',help='maximum number of words', type=int, default=1000)
    parser.add_argument('--bgcolor',help='background color', type=str, default='white')
    parser.add_argument('--out',help='image output name', type=str, default='out.png')

    args = parser.parse_args()
    # print(args.output)

    stop = read_words(args.stopwords) if args.stopwords else ""
    out = args.out if args.out.split('.')[-1] in ['png', 'jpg'] else args.out + '.png'

    wordcloud = PersianWordCloud(
        only_persian=args.persian,
        max_words=args.maxwords,
        stopwords=stop,
        margin=0,
        width=800,
        height=800,
        min_font_size=1,
        max_font_size=500,
        random_state=True,
        background_color="white",
        mask=read_img(args.mask)
    ).generate(read_file(args.txt))

    image = wordcloud.to_image()
    image.show()
    image.save(out)


if __name__ == '__main__':
    main()
    # txt = read_file('milad.txt')
    # print(txt)
    # word = read_words('milad.txt')
    # print(word)
    # img =read_img('images/hafez.png')
    # import matplotlib.pyplot as plt
    # plt.imshow(img)
    # plt.show()
