import sys

text = "welcome to code jam"
f = open(sys.argv[1], "r")
line = f.readline()
n = int(line.strip())
for i in xrange(n):
    variants = [0 for abs in xrange(len(text))]
    line = f.readline()
    for x, c in enumerate(line):
        for pos in xrange(len(text)):
            if c == text[pos]:
                if pos==0:
                    ac = 1
                else:
                    ac = variants[pos-1]
                variants[pos] += ac
            if variants[pos] == 0:
                break
    cases = variants[len(text)-1]
    print "Case #%d: %.4d" % (i+1, cases % 10000)

def empty():
    for i in xrange(n):
        variants = {}
        line = f.readline()
        for x, c in enumerate(line):
            if c == text[0]:
                variants[(x, 1)] = 1
            for last, pos in variants.keys():
                if pos<len(text) and c == text[pos]:
                    ac = variants[(last, pos)]
                    nc = variants.get((x, pos+1), 0)
                    variants[(x,pos+1)] = ac + nc
        filtered = filter(lambda x: x[0][1] == len(text), variants.items())
        cases = sum(map(lambda x: x[1], filtered))
        print "Case #%d: %.4d" % (i+1, cases % 10000)
