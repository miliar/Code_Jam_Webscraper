import sys

def solve(D, N, hs):
    ts = [(D - k)/float(v) for (k,v) in hs]
    mt = max(ts)

    return D / mt

testname = sys.argv[1]

print(testname)

fin = open(testname + '.in','r')
fout = open(testname + '.out','w')

ntest = int(fin.readline().strip())

for t in range (1, ntest + 1):
    line = fin.readline().strip().split()
    D = int(line[0])
    N = int(line[1])
    hs = []

    for i in range(0, N):
        line = fin.readline().strip().split()
        h = (int(line[0]), int(line[1]))
        hs.append(h)

    ans = solve(D, N, hs)
    fout.write("Case #{}: {}\n".format(t, ans))
