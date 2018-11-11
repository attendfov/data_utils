# _*_ coding:utf-8 _*_

import os
import sys
import numpy
import random
import numpy as np


def equal_func(a, b):
    return 1 if a == b else 0

def calc_rec_pr(score_list, grt_list, inf_list, equal_func=equal_func):

    assert (len(score_list)==len(grt_list))
    assert (len(score_list)==len(inf_list))

    assert (isinstance(score_list, (tuple, list)))
    assert (isinstance(grt_list, (tuple, list)))
    assert (isinstance(inf_list, (tuple, list)))

    score_list = [float(s) for s in score_list]
    equal_list = [int(equal_func(grt, inf)) for grt, int in zip(grt_list, inf_list)]
    zip_data = list(zip(score_list, equal_list))

    zip_data.sort(key=lambda x: x[0])

    epsion = 0.000001

    fp = epsion
    tp = epsion
    fn = epsion
    tn = epsion

    tp = tp + np.sum([1 if x==1 else 0 for x in equal_list])
    fp = fp + np.sum([1 if x==0 else 0 for x in equal_list])

    threshold = 0.00
    precision = round(tp/(tp+fp), 4)
    recall = round(tp/(tp+fp+fn), 4)

    threshold_list = []
    precision_list = []
    recall_list = []

    threshold_list.append(threshold)
    precision_list.append(precision)
    recall_list.append(recall)

    for data in zip_data:
        score, equal_value = data
        assert (equal_value in (0, 1))
        threshold_list.append(score)

        fn = fn + 1

        if 1==qual_value:
            tp = tp -1
        elif 0==equal_value:
            fp = fp -1

        precision = round(tp/(tp+fp), 4)
        recall = round(tp/(tp+fp+fn), 4)
        precision_list.append(precision)
        recall_list.append(recall)

    return precision_list, recall_list, threshold_list







