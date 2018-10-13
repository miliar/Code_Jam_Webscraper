# Time remaining to apocalypse
def apocalypse(events):
    T = gcd_n(intervals(events))
    return -events[0] % T

# Absolute values of the intervals between N numbers.
def intervals(z):
    return [abs(a-b) for a, b in zip(z, z[1:])]

# Greatest Common Divisor of N numbers.
def gcd_n(z):
    # gcd(a, b, c) = gcd(gcd(a,b), c)
    return reduce(gcd_2, z)

# Greatest Common Divisor of 2 numbers.
def gcd_2(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    try:
        cases = xrange(1, int(raw_input())+1)
        for case in cases:
            line = map(int, raw_input().split())
            n, events = line[0], line[1:]
            assert n == len(events)
            print "Case #%d: %d" % (case, apocalypse(events))
    except:
        print "INVALID INPUT"
            
main()
