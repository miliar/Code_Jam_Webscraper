import sys

T = int(sys.stdin.readline())

for k in range(1, T+1):
    ans1 = int(sys.stdin.readline())
    arr1 = []
    for i in range(4):
        str = sys.stdin.readline()
        r = str.split()
        arr1.append(r)
    ans2 = int(sys.stdin.readline())
    arr2 = []
    for i in range(4):
        str = sys.stdin.readline()
        r = str.split()
        arr2.append(r)

    ans1 -= 1
    ans2 -= 1

    match = []
    for x in arr1[ans1]:
        if x in arr2[ans2]:
            match.append(x)

    if len(match) == 1:
        print 'Case #%d: %s' % (k, match[0])
        continue
    if len(match) > 1:
        print 'Case #%d: Bad magician!' % k
    if len(match) == 0:
        print 'Case #%d: Volunteer cheated!' % k
