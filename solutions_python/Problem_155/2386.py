import sys, os

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

case = 1
fin.readline()
for l in fin:
    m, k = l.split()
    s = int(k[0])
    print "Case: ",case
    n = 0
    for i in xrange(1, len(k)):
        v = int(k[i])
        add = i - s
        if add > 0:
            print "  add i = {} v = {} s = {} add = {}".format(i, v, s, add)
            n += add
        s += v + max(0, add)
    print " needed = ",n
    fout.write("Case #{}: {}\n".format(case, n))
    case += 1

    
