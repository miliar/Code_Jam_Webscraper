# filename = "a.in"
filename = "aLarge.in"
outputFilename = "output.txt"


def solve(f):
    d, n = map(int, f.readline().strip().split(" "))
    time = 0
    for i in range(n):
        k, s = map(int, f.readline().strip().split(" "))
        t = (float(d) - float(k)) / float(s)
        time = max(t, time)

    return "{:.6f}".format(float(d) / float(time))


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
