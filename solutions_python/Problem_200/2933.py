import sys

in_fname = sys.argv[1]

fin = open(in_fname, 'r')
T = int(fin.readline())

out_fname = in_fname.split('.')[0] + '.out'
fout = open(out_fname, 'w')

for t in xrange(1, T + 1):
    N = fin.readline()
    N = str(int(N))

    n = len(N)

    ans = ''
    for i in xrange(n):
        for j in xrange(10, -1, -1):
            if int(ans + (str(j) * (n - i))) <= int(N):
                ans += str(j)
                break

    fout.write('Case #%d: %d\n' % (t, int(ans)))

