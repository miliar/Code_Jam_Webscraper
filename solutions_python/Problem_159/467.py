__author__ = 'Mohan.Rajendran'
maxRate = 0

def solve(inp):
    global maxRate
    N = int(inp.readline())
    X = map(int, inp.readline().split())
    maxRate = 0
    return first(X) + " " + second(X)

def first(X):
    global maxRate
    count = 0
    for i in xrange(len(X) - 1):
        a = X[i]
        b = X[i+1]
        if b < a:
            count += (a - b)
            if (a-b) > maxRate:
                maxRate = a-b
    return str(count)

def second(X):
    global maxRate
    count = 0
    for i in xrange(len(X) - 1):
        a = X[i]
        b = X[i+1]
        if a < maxRate:
            count += a
        else:
            count += maxRate
    return str(count)

if __name__ == "__main__":
    fileName = "large"
    inp = open(fileName + '.in', 'r')
    outp = open(fileName + '.out', 'w')

    cases = int(inp.readline())

    for case in xrange(1, cases+1):
        outp.write("Case #%i: %s\n" % (case, solve(inp)))

    inp.close()
    outp.close()