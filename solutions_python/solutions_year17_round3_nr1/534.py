import fileinput
import logging
import sys
import math

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

lines =[]

for line in fileinput.input():
    lines.append(line)

i=0
while i < len(lines):
    line = lines[i]
    if i == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        a = line.split()
        #print a
        # print line, i, a
        N = int(a[0])
        K = int(a[1])
        b= []
        for x in xrange(N):
            i = i+1
            a = lines[i].rstrip().split()
            b.append([int(a[0]),int(a[1])])
        instances.append((N,K,b))
    i = i+1

def empty(line):
    for i in xrange(len(line)):
        # print line[i],i
        if line[i] != '?':
            #print "returning", False
            return False
    #print "returning", True
    return True



def side(x):
    return x[0]*x[1]*2

def top(x):
    return x[0]*x[0]

def area(x):
    return side(x) + top(x)


from collections import defaultdict
from heapq import *

def instance(inst):
    N= inst[0]
    K=inst[1]
    cakes = sorted(inst[2],key=lambda x: x[0])
    #cakes = inst[2]
    q = []
    a=0
    cur_area = 0.0
    #print cakes
    for l in range(0,K):
        a = side(cakes[l])
        heappush(q,(a,l))
        cur_area +=a

    cur_area += top(cakes[K-1])
    max_area = cur_area
    last_top = top(cakes[K-1])

    for l in xrange(K,N):
        #print cakes,l,q
        #print cur_area,max_area
        cake = cakes[l]
        l -= top(cake)
        cur_area -= last_top
        last_top = top(cake)
        cur_area += area(cake)
        pair = heappop(q)
        cur_area -= pair[0]
        if cur_area > max_area:
            max_area = cur_area
        heappush(q,(side(cake),l))

    return max_area*math.pi
                

out_line_no = 1
for x in instances:
    result = instance(x)
    print "Case #%d: %.10f" % (out_line_no, result)
    out_line_no +=1



