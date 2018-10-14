import math

sets = []

with open("/Users/manuel/Desktop/test/codejam/03/C-small-2-attempt0.in", "r") as f:
    w = f.read().split("\n")
    for x in range(1, int(w[0]) + 1):
        r = w[x].split(" ")
        sets.append((int(r[0]), int(r[1])))


def formula(n, k):
    n += 1 - (k - math.pow(2, math.floor(math.log2(k))))
    k += 1
    steps = math.pow(2, math.ceil(math.log2(k) - 1))
    return (math.floor((n - 0.1) / math.pow(2, math.ceil(math.log2(k)))), math.floor((n - steps - 0.1) / (2 * steps)))


def run(s):
    return formula(s[0], s[1])


i = 0
for s in sets:
    i += 1
    print("Case #" + str(i) + ": " + " ".join(str(x) for x in run(s)))


def hui():
    def bad(n, k):
        m = me(n, k + 1)[0][-1]
        return (m[0], m[1])

    def formula(n, k):
        n += 1 - (n - math.pow(2, math.floor(math.log2(n))))
        k += 1
        steps = math.pow(2, math.ceil(math.log2(k) - 1))
        return (math.floor((n - 0.1) / math.pow(2, math.ceil(math.log2(k)))), math.floor((n - steps - 0.1) / (2 * steps)))

    def inner(k):
        cntb = -1
        difb = -1
        prevb = bad(k, k)
        cntf = -1
        diff = -1
        prevf = formula(k, k)
        for x in range(k, 256):
            b, f = bad(x, k), formula(x, k)
            if b != prevb:
                prevb = b

                if cntb > 0:
                    difb = x - cntb

                cntb = x

            if f != prevf:
                prevf = f

                if cntf > 0:
                    diff = x - cntf

                cntf = x

            if difb > 0 and diff > 0 and (cntf - cntb != 0):
                print("k " + str(k) + " x " + str(cntf) + " " + str(cntb) + " is " + str(cntb - cntf))
                difb = -1
                diff = -1

    for x in range(64, 128):
        inner(x)


hui()


i = 0
for s in sets:
    i += 1
    print("Case #" + str(i) + ": " + bad(s[0], s[1]))


def getout(arr, ind):
    if ind < len(arr):
        return str(arr[ind][1]).rjust(2, " ") + " " + str(arr[ind][0]).rjust(2, " ")
    else:
        return " " * 5


def printme(n):
    par = [me(x, x) for x in range(1, n)]

    for y in range(len(par[-1][0])):
        lstr = ""
        for x in par:
            lstr += getout(x[0], y) + " # "
        print(lstr)


def thing(n):
    steps = math.pow(2, math.ceil(math.log2(n + 1) - 1))
    print("steps", steps)
    for x in range(n - 1):
        print("x x")
    for x in range(n + (1 if n % 2 == 0 else 0), 32):
        print(math.floor((x - 0.1) / (2 * steps)), math.floor((x - steps - 0.1) / (2 * steps)))
