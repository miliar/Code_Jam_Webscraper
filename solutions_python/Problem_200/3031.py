import numpy
lines = open('small.input', 'r').read().splitlines()
t = int(lines[0])

with open('output.txt', 'w') as out:
    for number in range(t):
        l = lines[number+1]
        while True:
            tl = numpy.array(list(l))
            length = len(tl)
            c = False
            for i in range(1, length):
                if not tl[i-1] <= tl[i]:
                    tl[i-1] = int(tl[i-1]) - 1
                    tl[i:] = 9
                    c = True
                    l = list(tl)
                    break
            if not c:
                break

        print 'Case #{}: {}'.format(number+1, int(''.join(tl)))