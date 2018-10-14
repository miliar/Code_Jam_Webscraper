from sys import stdin


def main():
    t = int(stdin.readline().strip())
    for k in xrange(1, t+1):
        d, n = (int(s) for s in stdin.readline().strip().split(' '))
        k_s = [[int(s) for s in stdin.readline().strip().split(' ')]
               for _ in xrange(n)]
        t = max((d-k)/float(s) for k, s in k_s)
        print "Case #{}: {}".format(k, d/t)

main()
