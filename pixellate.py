# _____________________________________________________________________________
# pixellate.py - Creates a pixellated image from a source image.
# _____________________________________________________________________________

import cv2
import sys
import numpy
MAXGREY = 256

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def pixellate(image, mask):
    tmp_b = []
    tmp_g = []
    tmp_r = []
    hist_b = numpy.zeros(MAXGREY)
    hist_g = numpy.zeros(MAXGREY)
    hist_r = numpy.zeros(MAXGREY)
    idx = mask // 2
    sizes = image.shape
    pixellated_img = numpy.zeros(sizes)
    ny = sizes[0]
    nx = sizes[1]
    for y in range(idx, ny - idx, mask):
        for x in range(idx, nx - idx, mask):
            for i in range(-idx, idx + 1):
                for j in range(-idx, idx + 1):
                    if(not(i == idx and j == idx)):
                        tmp_b.append(image[y + i, x + i, 0])
                        tmp_g.append(image[y + i, x + i, 1])
                        tmp_r.append(image[y + i, x + i, 2])
            for i in range(0, mask**2 - 1):
                hist_b[int(tmp_b[i])] += 1
                hist_g[int(tmp_g[i])] += 1
                hist_r[int(tmp_r[i])] += 1
            i = 0
            j = 0
            k = 0
            b_sum = 0
            g_sum = 0
            r_sum = 0
            while(b_sum < 5):
                b_sum = b_sum + hist_b[i]
                i += 1
            while(g_sum < 5):
                g_sum = g_sum + hist_g[j]
                j += 1
            while(r_sum < 5):
                r_sum = r_sum + hist_r[k]
                k += 1
            for t_i in range(-idx, idx + 1):
                for t_j in range(-idx, idx + 1):
                    pixellated_img[y + t_i, x + t_j, 0] = i - 1
                    pixellated_img[y + t_i, x + t_j, 1] = j - 1
                    pixellated_img[y + t_i, x + t_j, 2] = k - 1
            for i in range(0, mask**2 - 1):
                hist_b[int(tmp_b[i])] = 0
                hist_g[int(tmp_g[i])] = 0
                hist_r[int(tmp_r[i])] = 0
            tmp_b = []
            tmp_g = []
            tmp_r = []

    return pixellated_img
# -----------------------------------------------------------------------------
# Main program.
# -----------------------------------------------------------------------------


if len(sys.argv) < 2:
    print(f"No image file. Usage :{sys.argv[0]} <image> <mask>")
    sys.exit(1)
if len(sys.argv) < 3:
    print(f"No mask parameter. Usage :{sys.argv[0]} <image> <mask>")
    sys.exit(1)

image = cv2.imread(sys.argv[1])
mask_value = int(sys.argv[2])

if mask_value % 2 == 0 or mask_value < 3:
    print("Mask parameter should be odd and bigger than 2. -> 3, 5, 7... etc. ")
    sys.exit(1)

image_out = pixellate(image, mask_value)
cv2.imwrite(sys.argv[2] + "x" + sys.argv[2] + "_pixellated_" + sys.argv[1], image_out)
# -----------------------------------------------------------------------------
# End of pixellate.py
# -----------------------------------------------------------------------------
# _____________________________________________________________________________
# TITLE - pixellate.py
# AUTHOR - Ogulcan Ozer.
# C_DATE - 19 MAY 2020
# U_DATE - 7 AUG 2020
# _____________________________________________________________________________
