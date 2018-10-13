import sys

if len(sys.argv) < 2:
    print "Usage: a.py input"
    exit()

input = sys.argv[1]
f = open(input)
T = f.readline()
T = int(T)

def paths(diag, cl, acc, r):
    if diag[cl - 1]:
        for c in diag[cl - 1]:
            paths(diag, c, acc + [cl], r)
    else:
        acc += [cl]
        r += [(acc[0], acc[-1])]

for i in range(T):
    # s = f.readline().strip("\n").split(" ")
    N = int(f.readline().strip("\n"))
    classes = [[]] * N
    r = []
    result = "No"

    for j in range(N):
        s = f.readline().strip("\n").split(" ")
        for l in range(len(s)):
            s[l] = int(s[l])
        classes[j] = s[1:]

    for k in range(N):
        paths(classes, k + 1, [], r)

    r.sort()

    last = None

    while r:
        current = r.pop()
        if last and current == last:
            result = "Yes"
        last = current

    print "Case #%d: %s" % (i + 1, result)
