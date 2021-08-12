import os


# # this installs the right pip and dependencies for the fresh python
os.system('conda install ipython pip')
os.system('conda install python=3.7')
# maskrcnn_benchmark and coco api dependencies
os.system('pip install ninja yacs cython matplotlib tqdm opencv-python h5py ')
#install utils
os.system('pip install -U scikit-learn')
os.system('pip install json')
# install pytorch
os.system('conda install -c pytorch pytorch-nightly=1.0.0 torchvision=0.2.2')
os.system("pip install 'pillow<7.0.0'")

# install pycocotools
os.system('cd ..')
os.system('git clone https://github.com/cocodataset/cocoapi.git')
os.system('cd cocoapi/PythonAPI')
os.system('python setup.py build_ext install')

# install apex
os.system('cd ..')
os.system('cd ..')
os.system('git clone https://github.com/NVIDIA/apex.git')
os.system('cd apex')
os.system('git checkout f3a960f80244cf9e80558ab30f7f7e8cbf03c0a0')
os.system('python setup.py install --cuda_ext --cpp_ext')
os.system('cd ..')

# install VC
os.system('git clone https://github.com/alfred100p/RPF.git')
os.system('cd VC-R-CNN')
os.system('python setup.py build develop')