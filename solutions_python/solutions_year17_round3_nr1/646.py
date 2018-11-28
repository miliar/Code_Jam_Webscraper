import sys
import math


def solve(N, K, ps):
    psa = []
    used = []

    for (r, h) in ps:
        ta = math.pi * r * r
        ca = 2 * math.pi * r * h

        psa.append((r, ta, ca))
        used.append(0)

    psa.sort()
    psa.reverse()

    maxxV = [0.0]

    def calculate(psa, used):
        sum = 0
        first = True

        for i in range(0, len(used)):
            if used[i] == 1:
                sum += psa[i][2]

                if first:
                    first = False
                    sum += psa[i][1]

        return sum

    def bt(pos, count, used):
        if count == K:
            nn = calculate(psa, used)
            if nn > maxxV[0]:
                maxxV[0] = nn

            return

        if pos == N:
            return

        bt(pos + 1, count, used)

        used[pos] = 1
        bt(pos + 1, count + 1, used)
        used[pos] = 0

    bt(0, 0, used)

    return maxxV[0]

testname = sys.argv[1]

print(testname)

fin = open(testname + '.in', 'r')
fout = open(testname + '.out', 'w')

ntest = int(fin.readline().strip())

for t in range(1, ntest + 1):
    line = fin.readline().strip().split()
    N = int(line[0])
    K = int(line[1])

    ps = []
    for i in range(0, N):
        line = fin.readline().strip().split()
        ps.append((int(line[0]), int(line[1])))

    ans = solve(N, K, ps)
    fout.write("Case #{}: {}\n".format(t,ans))