 The script finds the median intensity in a mask for all three color channels and replaces the masked region with the found median.
 Can be used to create pixel art from real life images.

 ## Example outputs :
| The original image. | Output with 3x3 mask.| Output with 5x5 mask.
:-------------------------:|:-------------------------:|:-------------------------:
<img src="./images/lenna.png" width="250">  |  <img src="./images/3x3_pixellated_lenna.png" width="250"> |  <img src="./images/5x5_pixellated_lenna.png" width="250">
| Output with 7x7 mask.| Output with 11x11 mask.| Output with 15x15 mask.
<img src="./images/7x7_pixellated_lenna.png" width="250">  |  <img src="./images/11x11_pixellated_lenna.png" width="250"> |  <img src="./images/15x15_pixellated_lenna.png" width="250">


### Usage :
```
pixellate.py <image> <mask>
-
pixellate.py lenna.png 5
```
