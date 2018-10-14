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
        k = int(a[1])
        n = int(a[0])
        instances.append((n,k))
    line_no+=1

def instance(inst):
    cnt = 0
    n = inst[0]
    k = inst[1]

    level = 0
    z = 1
    while 2*z-1 < k:
        z = 2*z
        level += 1

    # print level
    # print z

    kprime = z-1

    spaces_left = n-kprime
    avg_length_floor = int(spaces_left/(kprime+1))
    
    interval_length = avg_length_floor

    if (k-kprime) <= spaces_left%(kprime+1):
        interval_length +=1
    #print interval_length
    if ((interval_length-1)%2 == 0):
        return((interval_length-1)/2,(interval_length-1)/2)
    else:
        return((interval_length-1)/2+1,(interval_length-1)/2)

out_line_no = 1
for x in instances:
    z = instance(x)
    print "Case #%d: %d %d" % (out_line_no, z[0],z[1])
    out_line_no+=1


