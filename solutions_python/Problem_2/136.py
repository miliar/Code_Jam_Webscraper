import sys
import time

f = open(sys.argv[1])

o = open(sys.argv[1].split('.')[0] + '.out', 'w')

nCases = int(f.readline().strip())

for case in range(nCases):
    turnaround = int(f.readline().strip())
    (nA, nB) = map(int, f.readline().strip().split())

    times = []

    for i in range(nA):
        dep, arr = map(time.strptime, f.readline().strip().split(), ['%H:%M', '%H:%M'])
        # Fix daylight savings time strangeness
        dep = time.localtime(time.mktime(dep))
        arr = time.localtime(time.mktime(arr) + turnaround*60)
        times.append((dep, 'd', 'A'))
        times.append((arr, 'a', 'B'))

    for i in range(nB):
        dep, arr = map(time.strptime, f.readline().strip().split(), ['%H:%M', '%H:%M'])
        dep = time.localtime(time.mktime(dep))
        arr = time.localtime(time.mktime(arr) + turnaround*60)
        times.append((dep, 'd', 'B'))
        times.append((arr, 'a', 'A'))

    times.sort()

    currentA = 0
    currentB = 0

    totalA = 0
    totalB = 0

    #print times

    for t in times:
        if t[1] == 'a':
            if t[2] == 'A':
                currentA += 1
            else:
                currentB += 1
        else:
            if t[2] == 'A':
                if currentA > 0:
                    currentA -= 1
                else:
                    totalA += 1
            else:
                if currentB > 0:
                    currentB -= 1
                else:
                    totalB += 1

    #print 'Case #%d: %d %d\n' % (case + 1, totalA, totalB)
    o.write('Case #%d: %d %d\n' % (case + 1, totalA, totalB))
