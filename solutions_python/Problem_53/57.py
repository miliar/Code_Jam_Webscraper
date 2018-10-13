import sys

def ints(): return [int(x) for x in sys.stdin.readline().split()]

[T] = ints()

for i in xrange(T):
    n, k = ints()
    on = (1 << (n)) - 1
    step = on + 1
    print ("Case #%d: %s" % (i+1, "ON" if k >= on and ((k-on) % step) == 0 else "OFF"))
