import sys

def partitions(l):
    if not l:
        yield []
        return
    for i in xrange(2 ** len(l)):
        parts = [list(), list()]
        for item in l:
            parts[i & 1].append(item)
            i >>= 1
        yield parts

def patrick_add(a, b):
    ba = [int(x) for x in bin(a)[2:]]
    bb = [int(x) for x in bin(b)[2:]]
    
    p = len(bb) - len(ba)
    if p > 0:
        ba = ([0] * p) + ba
    elif p < 0:
        bb = ([0] * (p * -1)) + bb
    
    r = []
    for i in xrange(len(bb)):
        r.append(ba[i] ^ bb[i])
    r.reverse()
    v = 0
    for i in xrange(len(r)):
        p = 1 << i
        v += (r[i] * p)
    return v
    
f = open(sys.argv[1])
output_file = sys.argv[1].replace("in", "out")
output = open(output_file, "w")
T = int(f.readline().strip())

for i in xrange(T):
    N = int(f.readline().strip())
    cands = [int(c) for c in f.readline().strip().split(" ")]
    
    print "%s: %s" % (i, cands)
    
    max_value = None
    for p in partitions(cands):
        (sean_part, patrick_part) = p
        if len(patrick_part) == 0 or len(sean_part) == 0:
            continue
        
        sean_real_value = sum(sean_part)
        if max_value is not None and sean_real_value < max_value:
            continue
        patrick_real_value = sum(patrick_part)
        
        sean_value = reduce(patrick_add, sean_part)
        patrick_value = reduce(patrick_add, patrick_part)  
        
        #print "Sean %s: %s %s" % (sean_part, sean_real_value, sean_value)
        #print "Patrick %s: %s %s" % (patrick_part, patrick_real_value, patrick_value)  
                    
        if sean_value == patrick_value and (max_value is None or sean_real_value > max_value):
            #print "Update max value", sean_real_value
            max_value = sean_real_value
    if max_value is None:
        o = "Case #%s: NO\n" % (i + 1)
    else:
        o = "Case #%s: %s\n" % (i + 1, max_value)
    print o,
    output.write(o)