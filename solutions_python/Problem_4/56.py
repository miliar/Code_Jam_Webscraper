import sys,os,glob

def scalar_product(v1,v2):
    return sum([a1 * a2 for (a1,a2) in zip(v1,v2)])

def figure(v1,v2):
    #~ print v1
    #~ print v2
    v1.sort()
    v2.sort(reverse=True)
    return scalar_product(v1,v2)


if __name__=='__main__':
    xxx = open(sys.argv[1]).readlines()

    #~ print xxx
    T = int(xxx.pop(0))
    #~ print T

    for i in range(T):
        #~ print "case",i
        n = int(xxx.pop(0))
        #~ print n
        #~ for j in range(n):
            #~ print "engine",j
        #~ V.append((xxx.pop(0).split(), xxx.pop(0).split()))
        ret = figure([int(x) for x in xxx.pop(0).split()],
                      [int(x) for x in xxx.pop(0).split()])
        print "Case #%d: %d" % (i+1, ret)
        #~ print V

