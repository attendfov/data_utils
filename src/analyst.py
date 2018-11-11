# _*_ coding:utf-8 _*_


import os
import sys
import numpy
import random
import numpy as np


def align_name(name, align_len, padding='0'):
    assert (len(align_len)>0)

    src_name = str(name)
    pad_leng = max(0, align_len-len(src_name))
    dst_name = src_name + ''.join([padding for x in range(pad_leng)])
    return dst_name


def frequency_rec(value_list, start_value=0.0, end_value=1.0, step_value=0.01):

    step_name_list = []
    step_freq_list = []
    norm_freq_list = []

    s_value = start_value
    e_value = start_value + step_value

    while s_value<end_value:
        count = len([x for x in value_list if x>s_value and x<e_value])

        pre_name = align_name(s_value, 6)
        pos_name = align_name(e_value, 6)

        step_name_list.append(pre_name+'_'+pos_name)
        step_freq_list.append(count)

        s_value = e_value
        e_value = s_value+step_value


    sum = float(numpy.sum(step_freq_list))
    norm_freq_list = [count/sum for count in norm_freq_list]

    return step_name_list, step_freq_list, norm_freq_list









