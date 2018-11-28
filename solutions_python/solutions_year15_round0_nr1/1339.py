import sys
input = file(sys.argv[1])

def solve(s):
    ans = 0
    tot = 0
    for i, c in enumerate(s):
        c = int(c)
        if c and tot < i:
            ans += i - tot
            tot = i
        tot += c
    return ans

for case in range(int(input.readline())):
    values = [x for x in input.readline().split()]
    print "Case #%d: %d" % (case+1, solve(values[1]))
