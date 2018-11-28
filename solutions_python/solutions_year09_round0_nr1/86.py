import re;

l1 = raw_input()
vals = l1.split()
l = (int)(vals[0])
d = (int)(vals[1])
n = (int)(vals[2])

strs = []


for i in xrange(0, d):
    str = raw_input()
    strs.append(str)

# print strs

for i in xrange(0, n):
    str = raw_input().replace('(', '[').replace(')', ']')
    ctr = 0;
    # print str
    pattern = re.compile(str)
    for j in xrange(0, d):
        if re.match(pattern, strs[j]) != None:
            ctr = ctr+1;
    print "Case #%d: %d" % (i+1, ctr)
