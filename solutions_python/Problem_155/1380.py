from __future__ import division
from functools32.functools32 import lru_cache
import sys
import itertools
import os
import re
import string
import math
import sys
import heapq
from collections import namedtuple, defaultdict, deque
from Tools import gcj
from Tools.gcj import printd
from bitstring import BitArray, BitStream
from copy import deepcopy
from simpleai.search import SearchProblem, astar
import random
import operator
#from Tools import primes


def solver(shyness):
    need = 0
    people = 0
    for k in xrange(len(shyness)):
        #k is shyness level
        aud = int(shyness[k])
        #print("k",k,"aud",aud,"people",people,  "need", need)

        if k > people:
            need += k - people
            people += k - people
        people += aud
    return need


def reader(in_file):
    """
    @type in_file: gcj.FileWrapper
    """
    parts = in_file.getWords()
    s = parts[1]

    return {
        'shyness': s
    }


if __name__ == "__main__":
    ### GCJ module http://jamftw.blogspot.com.es/2012/05/python-code-jam-wrapper.html
    gcj.GCJ(reader, solver, os.getcwd(), "").run()
