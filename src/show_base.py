# _*_ coding:utf-8 _*_

import os
import sys
import numpy
import random
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageStat
from PIL import ImageFont

def PIL2CV(pil_image):
    return cv2.cvtColor(np.asarray(pil_image), cv2.COLOR_RGB2BGR)

def CV2PIL(cv_image):
    return Image.fromarray(cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB))


class ImageVis:

    @staticmethod
    def show_path(src_img_file, src_font_file, grt_text, inf_text, w_scale=2):
        assert (os.path.isfile(src_img_file))
        assert (os.path.isfile(src_font_file))

        ori_image = Image.open(src_img_file)
        imgw, imgh = ori_image.size

        text_size = int(min(48,max(16, min(imgw, imgh))))
        font_inst = ImageFont.truetype(src_font_file, text_size, encoding='unic')

        grt_image = np.ndarray((text_size+6, imgw*w_scale, 3), np.uint8)
        inf_image = np.ndarray((text_size+6, imgw*w_scale, 3), np.uint8)

        grt_text = grt_text if grt_text is not None else ''
        inf_text = inf_text if inf_text is not None else ''

        grt_image[:, :, :] = [150, 150, 150]
        inf_image[:, :, :] = [150, 150, 150]

        draw_grt_obj = ImageDraw.Draw(grt_image)
        draw_inf_obj = ImageDraw.Draw(inf_image)

        draw_grt_obj.text((3, 3), grt_text, font=font_inst, fill=(0, 0, 0))
        draw_inf_obj.text((3, 3), inf_text, font=font_inst, fill=(0, 0, 0))

        ori_imgh, ori_imgw = ori_image.shape[:2]
        grt_imgh, grt_ingw = grt_image.shape[:2]
        inf_imgh, inf_imgw = grt_image.shape[:2]

        assert (grt_ingw==inf_imgw)
        assert (grt_ingw>=ori_imgw)

        ori_image = PIL2CV(ori_image)
        grt_image = PIL2CV(grt_image)
        inf_image = PIL2CV(inf_image)

        image_w = np.max([ori_imgw, grt_ingw, inf_imgw])
        image_h = np.sum([ori_imgh, grt_imgh, inf_imgh])

        merge_image = np.ndarray((image_h, image_w, 3), np.uint8)

        h_off = 0
        merge_image[h_off:inf_imgh, 0:inf_imgw] = inf_image
        h_off = h_off + inf_imgh
        merge_image[h_off:ori_imgh, 0:ori_imgw] = ori_image
        h_off = h_off + ori_imgh
        merge_image[h_off:grt_imgh, 0:grt_ingw] = grt_image

        return merge_image
