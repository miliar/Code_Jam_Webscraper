import sys

def solve(N):
    sz = len(N)
    last = int(N[sz-1])

    for i in reversed(range(0, sz - 1)):
        cur = int(N[i])

        if cur > last:
            cur -= 1
            N[i] = str(cur)
            for j in range(i + 1, sz):
                N[j] = '9'

        last = cur

    if N[0] == '0':
        N[0] = ' '

    return "".join(N).strip()


testname = sys.argv[1]

print(testname)

fin = open(testname + '.in', 'r')
fout = open(testname + '.out', 'w')

ntest = int(fin.readline().strip())

for t in range(1, ntest + 1):
    line = fin.readline().strip().split()
    ans = solve(list(line[0]))
    fout.write("Case #{}: {}\n".format(t,ans))