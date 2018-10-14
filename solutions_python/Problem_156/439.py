f = open('B-large.in')
#f = open('test.in')
count = int(f.readline())
output = ''
for x in xrange(1, count + 1):
    pcount = int(f.readline())
    parr = f.readline().split()
    tmax = 0
    for i in xrange(0, pcount):
        tmax = max(tmax, int(parr[i]))
    tmin = tmax
    for j in xrange(1, tmax + 1):
        total = j
        for k in xrange(0, pcount):
            p = int(parr[k])
            if p > j:
                if p % j == 0:
                    total += (p / j - 1)
                else:
                    total += (p / j)
        tmin = min(tmin, total)
    output += 'Case #' + str(x) + ': ' + str(tmin) + '\n'

print(output)
newf = open('output.txt','w')
newf.write(output)
