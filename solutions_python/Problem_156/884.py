import sys
input = file(sys.argv[1])

def solve(v):
    v = sorted(v)[::-1]
    if v[0] == 1:
        return 1
    x = v[0]
    ass = max(v)
    for gg in range(2, x/2+1):
        vv = list(v)
        vv[0] -= gg
        vv.append(gg)
        ass = min(ass, solve(vv)+1)
    return ass

for case in range(int(input.readline())):
    input.readline()
    v = [int(x) for x in input.readline().split()]
    print "Case #%d: %d" % (case+1, solve(v))

