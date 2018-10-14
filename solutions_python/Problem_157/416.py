
import sys

cases = int(sys.stdin.readline())

basesymbols = ["1", "i", "j", "k"]
symbols = basesymbols + ["-"+x for x in basesymbols]

mult = {}
mult["1"] = {"1":"1", "i":"i" , "j":"j" , "k":"k" }
mult["i"] = {"1":"i", "i":"-1", "j":"k" , "k":"-j"}
mult["j"] = {"1":"j", "i":"-k", "j":"-1", "k":"i"}
mult["k"] = {"1":"k", "i":"j" , "j":"-i", "k":"-1"}



for i in basesymbols:
    for j in basesymbols:
        mult[i]["-"+j] = "-"+mult[i][j] if mult[i][j][0] != '-' else mult[i][j][1]
    mult["-"+i] = {}
    for j in symbols:
        mult["-"+i][j] = "-"+mult[i][j] if mult[i][j][0] != '-' else mult[i][j][1]

for case in xrange(1, cases+1):
    L, X = [int(x) for x in sys.stdin.readline().split()]
    st = list(sys.stdin.readline().strip()) * X
    # check the whole system comes to -1
    wholeval = reduce(lambda x, y: mult[x][y], st, "1")
    base = "1"
    leftindex = 0
    while (base != 'i' and leftindex < len(st)):
        base = mult[base][st[leftindex]]
        leftindex += 1
    base = "1"
    rightindex = len(st)-1
    while (base != 'k' and rightindex >= 0):
        base = mult[st[rightindex]][base]
        rightindex -= 1
    print "Case #%d: %s" % (case, "YES" if wholeval=="-1" and leftindex <= rightindex else "NO")

