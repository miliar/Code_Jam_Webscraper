
filename = 'A-large'

fin = open(filename + '.in')
fout = open(filename + '.out', 'w')
cases = int(fin.readline().strip())
for case in xrange(1, cases + 1):
    n, k = [int(x) for x in fin.readline().strip().split()]
    if k != 0: k = k % 2**n
    if k == 2**n - 1: ans = 'ON'
    else: ans = 'OFF'
    fout.write('Case #%d: %s\n' % (case, ans))
fin.close()
fout.close()
