def main():
    input = open("b.in",  "r")
    ntests = int(input.readline())

    for nt in xrange(1, ntests + 1):
        c, f, x = [float(value) for value in input.readline().split()]

        mini = x / 2
        t = c / 2
        n = 1
        while t + x / (2 + n * f) < mini:
            mini = t + x / (2 + n * f)
            t = t + c / (2 + n * f)
            n = n + 1

        print "Case #%d: %.7lf" % (nt, mini)

if __name__ == "__main__":
    main()
