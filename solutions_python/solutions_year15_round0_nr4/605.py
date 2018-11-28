import fileinput
import logging
import sys
import heapq
import math

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

D = 0

for line in fileinput.input():
    if line_no == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        a = line.split()
        instances.append((int(a[0]),int(a[1]),int(a[2])))
    line_no+=1

def check(X,R,C):
    logging.debug("Checking %d %d %d" %  (X, R, C))

    if X == 1:
        return "Gabriel"
    else:
        if X > R*C:
            return "Richard"
        elif (R*C)%X != 0:
            return "Richard"
        elif R==1:
            if (X <= 2):
                return "Gabriel"
            else:
                return "Richard"
        elif R==2:
            if (X <= 3):
                return "Gabriel"
            else:
                return "Richard"
        elif R==3:
            if (X <=3):
                return "Gabriel"
            else:
                return "Gabriel"
        elif R==4:
            if (X <= 2):
                return "Gabriel"
            else:
                assert(X != 3)
                return "Gabriel"
        else:
            assert(False)
                
table = {}

def pre_compute(lim):
    for R in xrange(1,lim):
        for C in xrange(1,lim):
            logging.debug("R: %d and C: %d" % (R,C))
            for X in xrange(1,lim):
                if X==1:
                    table[(X,R,C)] = "Gabriel"
                else:
                    if R < C:
                        table[(X,R,C)] = check(X,R,C)
                    else:
                        table[(X,R,C)] = check(X,C,R)
                    

def instance(inst):

    X = inst[0]
    R = inst[1]
    C = inst[2]
    return table[(X,R,C)]

pre_compute(5)

out_line_no = 1
for x in instances:
    logging.error("Instance %d" % out_line_no)
    print "Case #%d: %s" % (out_line_no, instance(x))

    out_line_no+=1



