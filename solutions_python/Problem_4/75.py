import sys

f = open(sys.argv[1])

o = open(sys.argv[1].split('.')[0] + '.out', 'w')

nCases = int(f.readline().strip())

for case in range(nCases):
    dimension = int(f.readline())

    v1 = map(int, f.readline().strip().split())
    v2 = map(int, f.readline().strip().split())

    v1.sort()
    v2.sort()
    v2.reverse()

    sum = 0
    for x,y in zip(v1, v2):
        sum += x*y

    o.write('Case #%d: %d\n' % (case + 1, sum))
