# About it 

`resizeImgForML` is a package for resize images for machie learning.

# Usage


 - put one directory path to detect all of images at the directory and resize for MNIST ML model

example code
```
from resizeImgForML import *
Resizer = Resizer()
img = Resizer.detectAllJpgImg("./")
Resizer.resizeBlackBackedMultipleImg(img,28)
```

 - put one path to detect image and resize for MNIST ML model

example code
```
from resizeImgForML import *
Resizer = Resizer()
img = Resizer.detectOneJpgImg("./output0.jpg")
Resizer.resizeBlackBackedOneImg(img,28)
```