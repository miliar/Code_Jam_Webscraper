import fileinput
import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)


nTest = 0
line_no = 0
instances = []

for line in fileinput.input():
    if line_no == 0:
        nTest = int(line)
        logging.debug("%d" % nTest)
    else:
        a = line.split()
        S = int(a[0])
        P = a[1]
        instances.append((S,P))
    line_no+=1


def instance(inst):

    cnt = 0
    a = inst[1]
    n = len(a)

    assert(len(a) == inst[0]+1)
    k = 0
    for i in xrange(n):
        cnt += int(a[i])
        if cnt <= i:
            k +=1 
            cnt += 1

    return k

out_line_no = 1
for x in instances:
    print "Case #%d: %d" % (out_line_no, instance(x))
    out_line_no+=1


