import math

filename = "a2.in"
outputFilename = "output.txt"


def solve(f):
    n, k = map(int, f.readline().strip().split(" "))
    if k == 1:
        return "{} {}".format(n/2, (n-1)/2)

    l = pow(2, int(math.log(k, 2)))
    print "l =", l
    p = n - (l - 1)
    print "p=", p
    x = p // l
    print "x =",x
    nx_1 = p % l
    print "nx_1 =", nx_1
    nx = l - nx_1
    print "nx=", nx
    ansMax = 0
    ansMin = 0
    if (k - l + 1) <= nx_1:
        print "---"
        ansMax, ansMin = (x + 1) / 2, (x)/2
        # ansMin = min(x/2, (x - 1)/2)
    else:
        ansMax, ansMin = (x) / 2, (x - 1) / 2


    return "{} {}".format(ansMax, ansMin)


def out(s, o):
    print s
    o.write("{}\n".format(s))


def main():
    f = open(filename)
    o = open(outputFilename, 'w+')
    T = int(f.readline())
    t = 1
    while t <= T:
        output = solve(f)
        out("Case #{}: {}".format(t, output), o)
        t+=1


if __name__ == "__main__":
    main()
