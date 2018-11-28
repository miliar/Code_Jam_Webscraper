
def solve1(mushroom):
    m = 0
    for k in range(len(mushroom)-1):
        if mushroom[k] > mushroom[k+1]:
            m += mushroom[k] - mushroom[k+1]
    return m

def highestSpeed(mushroom):
    v = 0
    for k in range(len(mushroom)-1):
        v = max(v, mushroom[k] - mushroom[k+1])
    return v

def solve2(mushroom):
    v = highestSpeed(mushroom)
    m = 0
    for k in range(len(mushroom)-1):
        m += min(v, mushroom[k])
    return m

fin = open('A-large.in')

caseNum = int(fin.readline())

for caseNo in range(caseNum):
    length = int(fin.readline())
    mushroom = list(map(int, fin.readline().strip().split()))
    print('Case #%d: %d %d' % (caseNo+1, solve1(mushroom), solve2(mushroom)))
fin.close()
