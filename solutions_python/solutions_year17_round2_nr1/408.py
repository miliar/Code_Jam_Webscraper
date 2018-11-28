__author__ = 'Christian'

from decimal import Decimal

#fname = 'test_a.txt'
#fname = 'A-small-attempt0.in'
fname = 'A-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')


T = int(data[0])
index = 0
for i in range(T):
    index += 1
    D, N = [Decimal(x) for x in data[index].split(' ')]
    times = []
    for j in range(N):
        index += 1
        Ki, Si = [Decimal(x) for x in data[index].split(' ')]
        times.append((D-Ki)/Si)
    print >> res_file, "Case #%s: %s" % (i+1, (D/max(times)).quantize(Decimal('0.000001')))
    
res_file.close()