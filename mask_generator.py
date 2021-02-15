import argparse
from persian_wordcloud.wordcloud import STOPWORDS, PersianWordCloud
from os import path
import cv2
import numpy as np







def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--image', help='main image file',
                        type=str, required=True)
    parser.add_argument('--thresh', help='threshold', type=int, required=False, default=125)
    parser.add_argument('--width', help='width of output image',type=int ,required=False, default=0)
    parser.add_argument('--height', help='height of output image',type=int ,required=False, default=0)
    parser.add_argument('--out', help='name of output image',required=False, default='mask.png')


    


    args = parser.parse_args()
    # print(args.output)
    im = cv2.imread(args.image)

    if args.width == 0 or args.height == 0:
        width, height = im.shape[:2]
    else:
        width, height = args.width, args.height

    
    grayImage = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Black white image', grayImage)
    (thresh, th2) = cv2.threshold(grayImage, args.thresh, 255, cv2.THRESH_BINARY)

    th2 = cv2.resize(th2, (width, height))
    # cv2.imshow('Black white image', th2)
    cv2.imwrite(args.out, th2)
    print("mask saved in ",args.out)
    # cv2.imshow('cropped',croped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()

