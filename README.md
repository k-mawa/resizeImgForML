# About it 

`resizeImgForML` is a package for resize images for machie learning.

# Usage 使い方

 - put one directory path to detect all of images at the directory and resize for MNIST ML model

同じディレクトリ内の複数のjpeg画像をMNIST学習モデルに読み込ませることができるように変換する

example code コード例

```
from resizeImgForML import *
Resizer = Resizer()
img = Resizer.detectAllJpgImg("./")
Resizer.resizeBlackBackedMultipleImg(img,28)
```

 - put one path to detect image and resize for MNIST ML model

ひとつのjpeg画像をMNIST学習モデルに読み込ませることができるように変換する

example code コード例

```
from resizeImgForML import *
Resizer = Resizer()
img = Resizer.detectOneJpgImg("./output0.jpg")
Resizer.resizeBlackBackedOneImg(img,28)
```

 - Get all png images in the same directory and convert to jpg (implemented from ver0.0.7)

同じディレクトリ内のpng画像を全部取得して、jpgに変換する(ver0.0.7より実装)

example code コード例

```
from resizeImgForML import *
resizer = Resizer()
imglist = resizer.detectAllPngImg("./")
resizer.convertPng2Jpg(imglist,".")
```

Jpg images are saved in the same directory with serial numbers.
When generating learning data from screenshots, it was sometimes png, so I implemented it.

同じディレクトリに連番でjpgイメージが保存されます。
スクリーンショットから学習データ生成する際はpngになっている場合があったので実装しました。