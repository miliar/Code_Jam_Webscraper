import sys

def find(x, ylist):
    n = len(ylist)
    idx = 0
    while idx < n and ylist[idx] <= x:
        idx += 1
    if idx >= n:
        idx = -1
    return idx

def war(xlist, ylist):
    score = 0
    for x in xlist:
        idx = find(x, ylist)
        if idx < 0:
            score += len(ylist)
            break
        else:
            ylist.pop(idx)
    return score

def deceitful_war(xlist, ylist):
    score = 0
    while len(ylist) > 0:
        y = ylist.pop(-1)
        idx = find(y, xlist)
        if idx >= 0:
            xlist.pop(idx)
            score += 1
        else:
            xlist.pop(0)
    return score

if __name__ == "__main__":
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')
    T = infile.readline()
    T = int(T.strip())
    for case in range(T):
        n = int(infile.readline().strip())
        line = infile.readline()
        naomi = map(float, line.strip().split())
        naomi.sort()
        line = infile.readline()
        ken = map(float, line.strip().split())
        ken.sort()
        z = war(naomi[:], ken[:])
        y = deceitful_war(naomi[:], ken[:])
        print >> outfile, 'Case #%d: %d %d' % (case + 1, y, z)
    infile.close()
    outfile.close()

