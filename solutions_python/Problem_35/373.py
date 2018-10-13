import sys
import fileinput

inf = 1e10000


def processInput():
    tcIn = fileinput.input()
    tcCount = int(tcIn.readline())
    for i in range(tcCount):
        rows, cols = (int(x) for x in tcIn.readline().split())
        altMap = []
        for r in range(rows):
            altMap.append([int(x) for x in tcIn.readline().split()])
        print "Case #%d:" % (i+1)
        #printMap(altMap)
        printMap(makeSinkMap(altMap),True)

def makeSinkMap(altMap):
    sinkMap = [[None for c in r] for r in altMap]
    label = 0
    for i, r in enumerate(altMap):
        for j, c in enumerate(r):
            f = flow(altMap, i, j)
            #print (i, j), altMap[i][j], f
            if not f:
                if not sinkMap[i][j]:
                    label += 1
                    sinkMap[i][j] = label
            else:
                if not sinkMap[i][j]:
                    if not sinkMap[f[0]][f[1]]:
                        label += 1
                        sinkMap[i][j] = label
                        sinkMap[f[0]][f[1]] = label
                    else:
                        sinkMap[i][j] = sinkMap[f[0]][f[1]]
                else:
                    if not sinkMap[f[0]][f[1]]:
                        sinkMap[f[0]][f[1]] = sinkMap[i][j]
                    else:
                        assert(sinkMap[f[0]][f[1]] != sinkMap[i][j])
                        sinkMap = mergeLabels(sinkMap, sinkMap[f[0]][f[1]], sinkMap[i][j])
                        label -= 1
    return sinkMap

def mergeLabels(m, l1, l2):
    minL = min(l1,l2)
    maxL = max(l1,l2)

    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c == l1 or c == l2:
                m[i][j] = minL
            if c > maxL:
                m[i][j] = c-1
    return m

def flow(m, x, y):
    n, w, e, s = (inf for i in range(4))
    if x > 0:
        n = m[x-1][y]
    if x < len(m)-1:
        s = m[x+1][y]
    if y > 0:
        w = m[x][y-1]
    if y < len(m[0])-1:
        e = m[x][y+1]

    minimum = min((n, w, e, s, m[x][y]))

    if minimum == m[x][y]:
        return None
    if minimum == n:
        return x-1, y
    if minimum == w:
        return x, y-1
    if minimum == e:
        return x, y+1
    if minimum == s:
        return x+1, y

def printMap(m, convert=False):
    for r in m:
        for c in r:
            if convert:
                print chr(c+96),
            else:
                print c,
        print

def main():
    processInput()

if __name__ == '__main__':
    status = main()
    sys.exit(status)
