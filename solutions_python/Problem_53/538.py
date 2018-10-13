import sys

fin  = sys.stdin
##fin  = file(r'A-large.in')
fout = sys.stdout
##fout = file(r'A-large.out', 'w')

def main():
    N = int(fin.readline())
    for i in xrange(N):
        ln = fin.readline()
        n, k = map(long, ln.split(' '))
        if (k % pow(2, n)) == pow(2, n) -1:
            result = "ON"
        else:
            result = "OFF"
        fout.write('Case #%d: %s\n' % (i +1, result))

main()
