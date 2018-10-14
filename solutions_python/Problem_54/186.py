def gcd(a, b):
    while b > 0: 
        a, b = b, a % b
    return a

def fun(cs):
    line = raw_input()
    a = [ int(x.strip()) for x in line.split(" ") ]

    assert(len(a) == a[0] + 1)

    n = a[0]
    data = a[1:]
    data.sort()

    x = data[1] - data[0]
    for i in xrange(1, n-1):
        x = gcd(x, data[i+1] - data[i])

    if data[0] % x == 0:
        y = 0
    else:
        y = x - (data[0] % x)

    print "Case #%d: %d" % (cs, y)


def main():
    T = int(raw_input())
    for i in xrange(T):
        fun(i+1)

if __name__ == "__main__":
    main()
