# mask_wordcloud

### Introduction
simple python script to easily generate wordcloud with arbitrary masks.
see below examples:
![ferdowsi](images/ferdowsi_cividis.png)
![hafez](images/hafez.png)
![saadi](images/saadi_word.png)
![shajarian](images/shajarian_wc.png)


### How to use
For creating wordcloud like these, you need to go three steps:
- choose your image for example for shajarian wordcloud I've choosed this image:
![shajarian](images/shajarian.jpg)

- run `mask_generator.py` script with appropriate arguments:

`python mask_generator.py --image <path_to_image_you_want>`
this script generate an image binary mask for you. example result:
![shajarian_mask](images/shm.png)


