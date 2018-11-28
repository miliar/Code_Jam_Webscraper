import sys

def read():
    return list(map(int, sys.stdin.readline().strip().split()))

def readm():
    return list(read() for i in range(4))

T, = read()
i = 1

while i <= T:
    r, = read()
    pos1 = readm()
    pos1 = pos1[r-1]
    r, = read()
    pos2 = readm()
    pos2 = pos2[r-1]

    inter = list(x for x in pos1 if x in pos2)

    if len(inter) == 0:
        ans = 'Volunteer cheated!'
    elif len(inter) == 1:
        ans = str(inter[0])
    else:
        ans = 'Bad magician!'

    print('Case #{}:'.format(i),ans)
    i += 1
