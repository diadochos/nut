#!/usr/bin/python
#
# Author: Peter Prettenhofer <peter.prettenhofer@gmail.com>
#
# License: BSD Style


"""
structlearn.util
================

"""
import operator
import functools
import numpy as np

from itertools import chain

def mask(instances, auxtask):
    count = 0
    for x in instances:
        indices = x['f0']
	for idx in auxtask:
	    if idx in indices:
		p = np.where(indices == idx)[0]
		if len(p) > 0:
		    x['f1'][p] = 0.0
		    count += 1
    return count

def autolabel(instances, auxtask):
    labels = np.ones((instances.shape[0],), dtype = np.float32)
    labels *= -1
    for i, x in enumerate(instances):
	indices = x['f0']
	for idx in auxtask:
	    if idx in indices:
		labels[i] = 1
		break
	
    return labels

def count(*datasets):
    if len(datasets) > 1:
	assert functools.reduce(operator.eq,[ds.dim for ds in datasets])
    counts = np.zeros((ds.dim,),dtype = np.uint16)
    for x, y in chain(*datasets):
	counts[x["f0"]] += 1
    return counts
