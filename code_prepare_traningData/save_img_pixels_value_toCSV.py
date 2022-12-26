# Convert pixels value of image to csv
import numpy as np
from PIL import Image
import cv2
import os
from string import Template

# IMG_DIR = './Img/'
# print(IMG_DIR)
for i in range(1, 301):
    STT = i
    # t = Template('./Img/img ($STT).jpg')
    t = Template('D:/Data_AI_Project/mat_nghieng/img ($STT).jpg')
    # print(t.substitute(STT=STT))
    path_after_sub = str(t.substitute(STT=STT))
    print(path_after_sub)

    img_array = cv2.imread(path_after_sub, cv2.IMREAD_GRAYSCALE)
    img_pil = Image.fromarray(img_array)
    img_28x28 = np.array(img_pil.resize((96, 96), Image.ANTIALIAS))
    # print(img_28x28)
    img_array = (img_28x28.flatten())
    img_array = img_array.reshape(-1, 1).T
    print(img_array)

    with open('side_img_enrich2.csv', 'ab') as f:

        np.savetxt(f, img_array, delimiter=",")
