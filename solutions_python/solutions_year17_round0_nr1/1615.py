from sys import stdin

def main():
    t = int(stdin.readline().strip())
    for k in xrange(1, t+1):
        s, n = stdin.readline().strip().split()
        s = [ch == '+' for ch in s]
        n = int(n)
        count = 0
        for i in xrange(len(s) - (n-1)):
            if not s[i]:
                # print "FLIP {}, {}".format(i, s)
                count += 1
                for j in xrange(n):
                    s[i+j] = not s[i+j]
                # print "AFTER: {}".format(s)
        if all(s[-(n-1):]):
            print "Case #{}: {}".format(k, count)
        else:
            print "Case #{}: IMPOSSIBLE".format(k)

main()
