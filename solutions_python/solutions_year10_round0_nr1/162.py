fin = open('small.in')
fout = open('small.out', 'w')

data = fin.readlines()
for x in xrange(len(data)):
    data[x] = (data[x])[:-1]

t = int(data[0])

for x in xrange(t):
    temp = data[x + 1].split(' ')
    n = int(temp[0])
    k = int(temp[1])
    check_num = 2**n
    k -= check_num - 1
    if k < 0:
        print >>fout, 'Case #' + str(x + 1) + ':', 'OFF'
    else:
        k = k % check_num
        if k == 0:
            print >>fout, 'Case #' + str(x + 1) + ':', 'ON'
        else:
            print >>fout, 'Case #' + str(x + 1) + ':', 'OFF'

fout.close()
fin.close()