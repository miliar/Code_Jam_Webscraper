import os, sys, re


#2 cookies per second
#C cookies = cost of cookie farm
#extra F cookies per second per farm
#X unspent cookies = victory
#C F X
#Format: \d+\.\d+

#recursive function f(s, c, f, x, n)
# s is current seconds
# c is farm cost
# f is addtl cookies/farm
# x is cookies to earn
# n is farms owned
# check seconds for victory
# check seconds for farm purchase
#        call self with additional farm
# return lowest seconds
# does increased rate offset C extra seconds
# if I keep my C cookies, can I get to X quicker?

def compare_times(s, c, f, x, n):
    solved = False
    while not solved:
        wait = s + (x / (2 + f * n))  # assume this is slower
        buy = s + (c / (2 + f * n)) + (x / (2 + f * (n + 1)))
        if wait < buy:
            return wait
        else:
            s = s + (c / (2 + f * n))
            n = n + 1

def magic(cases, data):
    ans = []
    for i in xrange(cases):
        ans.append(compare_times(0.0, data[i][0], data[i][1], data[i][2], 0))
    return ans


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit()
    with open(sys.argv[1], 'r') as f:
        t = int(f.readline().rstrip())
        x = []
        for l in f:
            l = [float(n) for n in re.split(r"\s", l.rstrip())]
            x.append(l)
        ans = magic(t, x)
        with open("{}_output".format(sys.argv[1]), 'w') as o:
            for a in xrange(t):
                o.write("Case #{}: {:.7f}\n".format(a + 1, ans[a]))