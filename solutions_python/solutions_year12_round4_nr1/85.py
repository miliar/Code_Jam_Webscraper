import sys

values = []

def minCross(vines, D, i):
    global values

    ret = (False, float('inf'))

    if sum(vines[i]) >= D:
        ret = (True, D - vines[i][0])

    for j in xrange(i+1, len(vines)):
        if sum(vines[i]) >= vines[j][0]:
            mcvj = values[j]
            if mcvj[0] and vines[j][0] - vines[i][0] >= mcvj[1]:
                ret = (True, min(ret[1], vines[j][0] - vines[i][0]))

    values[i] = ret
    return ret

def solve(vines, D):
    #print vines, D
    for i in reversed(xrange(len(vines))):
        #if sum(vines[i]) >= D:
        #print minCross(vines, D, i)
        minCross(vines, D, i)
    mcv0 = minCross(vines, D, 0)
    return (mcv0[0] and mcv0[1] <= vines[0][0])

def yesno(v):
    if v:
        return 'YES'
    else:
        return 'NO'

def main():
    global values
    with open(sys.argv[1]) as f:
        T = int(f.readline().strip())
        for i in xrange(T):
            N = int(f.readline().strip())
            values = [0]*N
            vines = []
            for j in xrange(N):
                d, l = [int(x) for x in f.readline().split()]
                vines.append((d, l))
            D = int(f.readline().strip())
            res = solve(vines, D)
            print 'Case #%d: %s' % (i+1, yesno(res))

if __name__ == "__main__":
    main()
