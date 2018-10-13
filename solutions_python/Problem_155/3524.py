import sys

f = open('input.txt', 'r')
# f = sys.stdin
sys.stdout = open('output.txt', 'w')

inp = f.readlines()

def codejamprint(string, i=[1]):
    print "Case #%d: %s" % (i[0], str(string))
    i[0] += 1

def count(string, Smax):
    c = 0
    additional = 0
    for i, si in enumerate(string.strip()):
        si = int(si)
        if si == 0: continue
        if c < i:
            additional += (i-c)
            c +=additional
        c+=si
    return additional


for t in range(int(inp.pop(0))):
    Smax, string = inp.pop(0).split(' ')
    codejamprint(count(string, Smax))

