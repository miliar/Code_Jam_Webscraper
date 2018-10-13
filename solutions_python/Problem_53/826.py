from sys import stdin

for case in range(1, int(stdin.readline()) + 1):
    (n, k) = [int(x) for x in stdin.readline().split()]
    c = 1 << n
    print "Case #%d: %s" % (case, 'ON' if k%c == c-1 else 'OFF')