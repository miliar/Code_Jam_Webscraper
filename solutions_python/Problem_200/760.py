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
        S = a[0]
        instances.append(S)
    line_no+=1


def instance(inst):
    cnt = 0
    a = list(inst)

    prev = a[0]
    i = 1
    while(i<len(a)):
        if (a[i] < prev):
            if (a[i-1] != '0'):
                a[i-1] = str(int(a[i-1])-1)
                for j in xrange(i,len(a)):
                    a[j] = '9'
                if i==1:
                    break
                i = i-2
            else:
                print "WTF: Should not have been tidy!",a
                exit(0)
        prev = a[i]
        i+=1

    return str(int(''.join(a)))

out_line_no = 1
for x in instances:
    print "Case #%d: %s" % (out_line_no, instance(x))
    out_line_no+=1


