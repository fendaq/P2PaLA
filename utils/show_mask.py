from __future__ import print_function
from builtins import range

import sys
import numpy as np
import cv2
try:
    import cPickle as pickle
except:
    import pickle as pickle

import matplotlib.pyplot as plt

def main():
    """
    Quick script to show mask images stored on pickle files
    """
    with open(sys.argv[1],'r') as fh:
        data = pickle.load(fh)
    if data.ndim == 2:
        plt.imshow(data)
    else:
        m = np.sqrt(data.ndim)
        rows= int(np.floor(m))
        cols= int(np.ceil(m))
        fig, axs = plt.subplots(rows,cols)
        fig.subplots_adjust(hspace = .5, wspace=.01)
        for n in range(data.ndim-1):
            axs[n].imshow(data[n])
            axs[n].set_title("dim="+str(n))
            
    plt.show()
    exit()

if __name__ == '__main__':
    if len(sys.argv) > 1 and  sys.argv[1] != '-h':
        main()
    else:
        print("Usage: python {} <pickle_file>".format(sys.argv[0]))
