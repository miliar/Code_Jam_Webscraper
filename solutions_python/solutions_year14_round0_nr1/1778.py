import sys

for i in range(int(sys.stdin.readline())):
    j = int(sys.stdin.readline()) - 1
    l = []
    for _ in range(4):
        l.append(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline()) - 1
    ll = []
    for _ in range(4):
        ll.append(map(int, sys.stdin.readline().split()))
    r = set(l[j]).intersection(ll[k])
    if len(r) == 1:
        print('Case #{}: {}'.format(i + 1, list(r)[0]))
    elif not r:
        print('Case #{}: Volunteer cheated!'.format(i + 1))
    else:
        print('Case #{}: Bad magician!'.format(i + 1))
