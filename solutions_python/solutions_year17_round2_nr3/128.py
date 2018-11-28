import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.ERROR)


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
        Q = int(a[1])
        b= []
        for x in xrange(N):
            i = i+1
            a = lines[i].rstrip().split()
            b.append([int(a[0]),int(a[1])])
        d = []
        for x in xrange(N):
            i = i+1
            a = lines[i].rstrip().split()
            d.append(map(int,a))
        e = []
        for x in xrange(Q):
            i = i+1
            a = lines[i].rstrip().split()
            e.append([int(a[0]),int(a[1])])
        instances.append((N,Q,b,d,e))
    i = i+1
                     
def empty(line):
    for i in xrange(len(line)):
        # print line[i],i
        if line[i] != '?':
            #print "returning", False
            return False
    #print "returning", True
    return True



def precompute(distances,horses):
    N = len(distances)
    times = [[-1 for x in xrange(N)] for x in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            if (i==j):
                pass
            else:
                if (distances[i][j] <= horses[i][0]) and (distances[i][j]>-1):
                    if (times[i][j] >=0):
                        times[i][j] = min(times[i][j],1.0*distances[i][j]/horses[i][1])
                    else:
                        times[i][j] = distances[i][j]/horses[i][j]

    return times

from collections import defaultdict
from heapq import *


# Modified from https://gist.github.com/kachayev/5990802

def time(dist,speed,left):
    if left < dist:
        return -1
    elif dist < 0:
        return -1
    else:
        return dist*1.0/speed
    
def find_time(pair,distances,horses):
    logging.debug("in find_time")
    seen = set()
    q = [(0,(pair[0]-1,pair[0]-1,horses[pair[0]-1][0]))]
    t = pair[1]-1
    while q:
        logging.debug(q)
        (cost,x) = heappop(q)
        (v1,h1,left) = x
        #logging.debug (v1,h1,left)
        if (v1,h1,left) not in seen:
            seen.add((v1,h1,left))
            if v1 == t: return cost
            for v2 in xrange(len(distances)):
                if v1==v2:
                    pass
                c = time(distances[v1][v2],horses[v1][1],horses[v1][0])
                new_left = horses[v1][0]-distances[v1][v2]
                if c>=0 and (v2,v1,new_left) not in seen:
                    heappush(q, (cost+c, (v2,v1,new_left)))
                c = time(distances[v1][v2],horses[h1][1],left)
                new_left = left-distances[v1][v2]
                if c>=0 and (v2,h1,new_left) not in seen:
                    heappush(q, (cost+c, (v2,h1, new_left)))
    return float("inf")


def instance(inst):
    N = inst[0]
    Q = inst[1]
    horses = inst[2]
    distances = inst[3]
    pairs = inst[4]

    logging.debug(horses)
    logging.debug(distances)
    logging.debug(pairs)
    
    result = []
    for i in xrange(len(pairs)):
        result.append(find_time(pairs[i],distances,horses))
    
    #print board
    return result
                

out_line_no = 1
for x in instances:
    result = instance(x)
    print "Case #%d:" % out_line_no, 
    for x in result:
        print x,
    print
    out_line_no +=1



