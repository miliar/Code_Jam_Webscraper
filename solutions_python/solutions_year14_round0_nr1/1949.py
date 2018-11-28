keis = int(raw_input())
for kei in xrange(keis):
    arr = []
    r1 = int(raw_input())
    for i in xrange(4):
        arr.append([int(x) for x in raw_input().split()])
    s1 = set(arr[r1-1])
    r2 = int(raw_input())
    arr = []
    for i in xrange(4):
        arr.append([int(x) for x in raw_input().split()])
    s2 = set(arr[r2-1])
    s = s1 & s2
    if len(s) == 1:
        print('Case #%d: %d' % (kei+1, s.pop(),))
    elif len(s) > 1:
        print('Case #%d: Bad magician!' % (kei+1,))
    else:
        print('Case #%d: Volunteer cheated!' % (kei+1,))
