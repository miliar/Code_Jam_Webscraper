
def recycle(a, b):
    pairs = set()
    for n in range(a, b + 1):
        strn = str(n)
        strm = str(n)
        for i in range(len(strn)):
            strm = strm[1:] + strm[0]
            if a <= n < int(strm) <= b and \
                    len(str(int(strn))) == len(str(int(strm))):
                pairs.add((strn, strm))
    return len(pairs)

# print recycle(1, 9)
# print recycle(10, 40)
# print recycle(100, 500)
# print recycle(1111, 2222)

import sys

filein = open(sys.argv[1])
fileout = open(sys.argv[2], 'w')

t = int(filein.readline().strip())

for i in range(1, t + 1):
    a, b = filein.readline().strip().split(" ")
    a, b = int(a), int(b)
    pairs = recycle(a, b)
    fileout.write("Case #%d: %d\n" % (i, pairs))

fileout.close()
