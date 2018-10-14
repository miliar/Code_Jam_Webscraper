import numpy


lines = open('large.in', 'r').read().splitlines()
test = int(lines[0])
out = open('output.txt', 'w')


for t in range(test):
    n = lines[t+1]
    while True:
        tidy = numpy.array(list(n))
        good = False
        for i in xrange(1, len(tidy)):
            if tidy[i-1] > tidy[i]:
                tidy[i-1] = int(tidy[i-1]) - 1
                tidy[i:] = 9                    # Fills all column ahead with 9
                good = True
                n = list(tidy)
                break
        if good is False:
            break
    temp = 'Case #%s: %d' % (t+1, int(''.join(tidy)))
    print temp
    out.write(temp+'\n')
out.close()
