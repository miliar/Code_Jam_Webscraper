def nCr(n, r):
    result = 1
    for x in xrange(n - r + 1, n + 1):
        result *= x
    for y in xrange(2, r + 1):
        result /= y
    return result

A = [[], [], [0, 1]]
XX = 25

for i in xrange(3, XX + 1):
    a = [0, 1] + [0]*(i - 2)
    for j in xrange(2, i):
        for k in xrange(j - 1, max(j - (i - j) - 1, 0), -1):
#        for k in xrange(1, j - 1)
#            if i == 6:
#                print j, k
            m = j - k - 1
            a[j] += nCr(i - j - 1, m)*A[j][k]
    A.append(a)
    print i
#    print '%d %d' % (i, sum(a))

for i in range(10):
    print sum(A[i])

INFILE = 'E:\\cj\\' + 'C' + '.in.txt'
OUTFILE = 'E:\\cj\\C' + '.out'

fin = open(INFILE, 'r')
lines = fin.readlines()
fin.close()

fout = open(OUTFILE, 'w')

case = 0
cases = int(lines[0])
ptr = 1
   
for case in xrange(1, cases + 1):
    n = int(lines[case])
    count = sum(A[n])          
    fout.write('Case #%d: %d\n' % (case, count%100003)) 

fout.close()
    
