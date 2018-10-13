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
        #print a
        S = a[0]
        run = int(a[1])
        instances.append((a[0],run))
    line_no+=1


def check(a):
    for x in xrange(len(a)):
        if a[x]=='-':
            return False
    return True

def instance(inst):
    cnt = 0
    a = list(inst[0])
    n = len(a)
    run = inst[1]

    count = 0

    for i in xrange(0,len(a)-run+1):
        if a[i] == '-':
            #print a
            count +=1 
            for j in xrange(0,run):
                if a[i+j] == '-':
                    a[i+j] = '+'
                else:
                    a[i+j] = '-'

    if check(a):
        return str(count)
    else:
        return 'IMPOSSIBLE'

out_line_no = 1
for x in instances:
    print "Case #%d: %s" % (out_line_no, instance(x))
    out_line_no+=1


