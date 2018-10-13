import sys

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    N = int(f.readline())
    values = [int(x) for x in f.readline().split()]
    expected = 0
    while True:
        segment = 0
        for i in range(0, len(values)):
            a = values[i]
            while values[a - 1] != a:
                temp = values[a - 1]
                values[a - 1] = a
                a = temp
                segment += 1
            if segment != 0:
                break
        if segment == 0:
            break
        expected += segment
    print "Case #%d: %0.6f" % (case + 1, expected)
