#!/usr/bin/python

import sys
import math	
import Queue
from datetime import datetime

startTime = datetime.now()
sys.setrecursionlimit(20000)

def readn(n):
	return [raw_input().strip() for i in range(n)]
def read():
	return raw_input().strip()
def readints():
	return map(int, read().split())
def readint():
	return readints()[0]
def wl(n, o):
	print("Case #{0}: {1}".format(n, o))
	
	
T = readint()
for TT in range(T):
    r, t = readints();

    root = (-2 * r + 1 + math.sqrt((2 * r - 1) * (2 * r - 1) + 8 * t)) / 4;

    wl(1+TT, int(math.floor(root)));
	
	
	
	
#print(datetime.now()-startTime)