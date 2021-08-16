import tensorflow as tf
import os
import numpy as np


splits=['train','val','test']

for split in splits:
  print(split)
  image_folder = 'RPF/images/MS-COCO-2014/'+split+'2014/'
  if not os.path.exists(path+''+ image_folder):
    image_zip = tf.keras.utils.get_file(split+'2014.zip',
                                        cache_subdir=os.path.abspath('RPF/images/MS-COCO-2014/'),
                                        origin = 'http://images.cocodataset.org/zips/'+split+'2014.zip',
                                        extract = True)
    PATH = os.path.dirname(image_zip) + image_folder
    os.remove(image_zip)
  else:
    PATH = os.path.abspath('RPF/images/MS-COCO-2014/') + image_folder
  
  img_list=os.listdir('RPF/images/MS-COCO-2014/'+split+'2014/')
  
  