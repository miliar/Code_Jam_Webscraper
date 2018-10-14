import sys

with open(sys.argv[1]) as f:
    T = int(f.readline())
    case = 1
    for line in f:

        line = line.strip().split(' ')
        slevels = line[1]
        #print slevels

        aux = 0
        tmp = 0
        for index, slevel in enumerate(slevels):
            if index > aux:
                aux += 1
                tmp += 1
            
            aux += int(slevel)

        print "Case #%d: %d" % (case, tmp)
        case += 1
