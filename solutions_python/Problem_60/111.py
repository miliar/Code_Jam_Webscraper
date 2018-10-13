import sys

def calcswap(n,k,b,t,Xs,Vs):
    if k == 0:
        return 0
    result = [ Vs[i] * t + Xs[i] - b for i in range(n)]
#    print result
    arrivable = [x for x in result if x >= 0]
#    print arrivable
    if len(arrivable) < k:
        return -1
    result.reverse()
    arrived,swaptarget,swapnum = 0,0,0
    for i in xrange(n):
        if result[i] >= 0:
            arrived += 1
            swapnum += swaptarget
            if arrived == k:
                break
        else:
            swaptarget += 1
    return swapnum

def readinput(fname):
    count,num = 0,0
    for i,line in enumerate(open(fname)):
        if i == 0:
            c = line.strip().split()[0]
            continue
        elif count < 1 :
            n,k,b,t = [int(x) for x in line.strip().split()]
#            print n,k,b,t
            num += 1
            count = 2
        elif count == 2:
            Xs = [int(x) for x in line.strip().split()]
            count -= 1
        elif count == 1:
            Vs = [int(x) for x in line.strip().split()]
            count -= 1
            s = calcswap(n,k,b,t,Xs,Vs)
            if s !=-1:
                print "Case #%d: %d"%(num,s)
            else:
                print "Case #%d: IMPOSSIBLE"%num

def main():
    readinput(sys.argv[1])

if __name__ == '__main__':
    main()