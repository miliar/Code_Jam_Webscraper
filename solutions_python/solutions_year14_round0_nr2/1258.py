import sys
readline = sys.stdin.readline
def solve(r, C, F, X):
    best_so_far = X/r
    time_so_far = 0
    n = 0
    while time_so_far < best_so_far:
        # print "n = %d, best_so_far = %f, time_so_far = %f, r = %f" % (n, best_so_far, time_so_far, r)
        best_so_far = min(best_so_far, time_so_far + X/r)
        time_so_far += C/r
        r += F
        n += 1
    return best_so_far

c = int(readline())
for i in range(c):
    c, f, x = map(float, readline().split())
    print "Case #%d: %.10f" % (i+1, solve(2., c, f, x))
