import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

class TableCut():
    def __init__(self, input_estimateimage):
        image_path = 'C:/Users/Kimyounghak/PycharmProjects/Ccompany/media/' + str(input_estimateimage)

        plot_flag = True
        save_output = True

        self.image = cv2.imread(image_path)

        gray_scale = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        th1, img_bin = cv2.threshold(gray_scale, 150, 225, cv2.THRESH_BINARY)

        img_bin = ~img_bin

        line_min_width = 15

        kernal_h = np.ones((1, line_min_width), np.uint8)
        kernal_v = np.ones((line_min_width, 1), np.uint8)

        img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)

        img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)

        img_bin_final = img_bin_h | img_bin_v

        final_kernel = np.ones((3, 3), np.uint8)
        img_bin_final = cv2.dilate(img_bin_final, final_kernel, iterations=1)

        ret, labels, stats, centroids = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8,
                                                                         ltype=cv2.CV_32S)

        y_list = []
        for i in range(len(stats)):
            y_list.append(stats[i][1])

        a_list = []
        b_list = []
        c_list = []
        for a, b, c in list(zip(y_list, y_list[1:], y_list[2:])):
            a_list.append(a)
            b_list.append(b)
            c_list.append(c)

        table_error = 5
        last_idx = []
        for i in range(len(y_list) - 2):
            if a_list[i] != b_list[i] != c_list[i] and abs(a_list[i] - b_list[i]) > table_error and abs(
                    b_list[i] - c_list[i]) > table_error:
                last_idx.append(i)

        want_idx = []
        for r in range(len(last_idx) - 1):
            if last_idx[r + 1] - last_idx[r] < table_error * 4:
                pass
            else:
                want_idx.append(last_idx[r + 1])
        result = stats[want_idx[0]]

        X = result[0]
        Y = result[1]
        W = result[2]
        H = result[3]

        img = cv2.imread(image_path)
        cropped_img = img[0: (Y + H), 0: (X + W)]

        if plot_flag:
            plt.plot(cropped_img)
        #     plot(img)

        self.cropped_img_1 = cv2.imwrite('cropped_img2.jpg', cropped_img)

    def plot(self, cmap=None):
        plt.figure(figsize=(15, 15))
        plt.imshow(self.image, cmap=cmap)
        return self.cropped_img_1

