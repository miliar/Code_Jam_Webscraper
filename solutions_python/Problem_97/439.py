import sys


def recycle(n):
    str_n = str(n)
    for i in xrange(1, len(str_n)):
        res = str_n[i:] + str_n[:i]
        if res[0] != '0':
            yield int(res)


with open(sys.argv[1]) as f:
    n_cases = f.readline()
    cases = [map(int, line.split(" ")) for line in f]


for i, case in enumerate(cases):
    a, b = case
    result = set()
    for n in range(a, b + 1):
        for r in recycle(n):
            if r > n and r <= b:
                result.add((n, r))
    #print result

    print "Case #%d: %s" % (i + 1, len(result))
