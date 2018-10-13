fin = open('E:\\cj\\A-large.in', 'r')
lines = fin.readlines()
fin.close()

fout = open('E:\\cj\\a-m.out', 'w')

eqmod = lambda a, b, x: a % x == b % x

case = 0
cases = int(lines[0])
for case in xrange(1, cases + 1):
    l = lines[case]
    N, K = [int(x) for x in l.split()]
       
    fout.write('Case #%d: %s\n' % (case, 'ON' if eqmod(K, -1, 2**N) else 'OFF'))

fout.close()
    
