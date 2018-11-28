import fileinput
import logging
import sys

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
        D = int(a[0])
        N = int(a[1])
        b= []
        for x in xrange(N):
            i = i+1
            a = lines[i].rstrip().split()
            b.append([int(a[0]),int(a[1])])
        instances.append((D,N,b))
    i = i+1

def empty(line):
    for i in xrange(len(line)):
        # print line[i],i
        if line[i] != '?':
            #print "returning", False
            return False
    #print "returning", True
    return True

def instance(inst):
    D = inst[0]
    N = inst[1]
    horses = inst[2]

    logging.debug(horses)
    result = min([(x[1]*1.0*(D*1.0)/(D-x[0])) for x in horses]) 

    #print board
    return result
                

out_line_no = 1
for x in instances:
    result = instance(x)
    print "Case #%d: %.10f" % (out_line_no, result)
    out_line_no +=1



