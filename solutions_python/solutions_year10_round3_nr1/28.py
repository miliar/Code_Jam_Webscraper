import sys

fname = sys.argv[1].replace(".in","")
fin = open(fname+'.in', 'rU')
fout = open(fname+'.out', 'w')

T = int(fin.readline().strip())

for case in xrange(T):
    N = int(fin.readline().strip())
    A,B, ans = [], [], 0
    for i in xrange(N):
        a,b = map(int, fin.readline().split())
        A.append(a)
        B.append(b)
    for i in xrange(N):
        for j in xrange(i+1,N):
            if (A[i] < A[j] and B[i] > B[j]) or (A[i] > A[j] and B[i] < B[j]):
                ans += 1
    fout.write("Case #%i: %s\n" % (case+1, ans))

fin.close()
fout.close()