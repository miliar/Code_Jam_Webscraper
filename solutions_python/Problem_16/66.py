from sys import argv

f = open(argv[1])

def solveCase(string, blocksize):
    c = [i for i in range(blocksize)]
    largest = 123456789234567
    for p in permute(c):
        temp = compress(string, p)
        if temp < largest:
            largest = temp
    return largest #"".join([str(i + 1) for i in blarg])

def permute(c):
    if len(c) <=1:
        yield c
    else:
        for p in permute(c[1:]):
            for i in range(len(p) + 1):
                yield p[:i] + c[0:1] + p[i:]


def compress(s, c):
    chars = []
    slen = len(s)
    clen = len(c)
    groups = slen / clen
    for i in range(groups):
        for j in c:
            chars.append(s[i * clen + j])

    prev = None
    comp = 0
    for char in chars:
        if char != prev:
            prev = char
            comp += 1
    return comp

cases = int(f.readline())
for i in range(cases):
    blocksize = int(f.readline())
    string = f.readline()[:-1]
    solution = solveCase(string, blocksize)
    print "Case #%s: %s" % ((i + 1), solution)
