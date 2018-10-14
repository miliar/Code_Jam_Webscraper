'''
Created on 7 maj 2011

@author: rickard
'''
import sys

# For checking only
ELEM = "QWERASDF"
NONBASE = ''.join([chr(x) for x in range(ord('A'),ord('Z')+1) if not chr(x) in ELEM])

def testcase(tc):
    tc = tc.split()
    ncombines = int(tc[0])
    combines = tc[1:ncombines+1]
    assert all(len(c) == 3 for c in combines)
    assert all(c[0] in ELEM and c[1] in ELEM and c[2] in NONBASE for c in combines)
    # Recombine into a unique lookup
    combines = dict((min(c[0],c[1])+max(c[0],c[1]),c[2]) 
                     for c in combines)
    assert len(combines) == ncombines
    
    nopposing = int(tc[ncombines+1])
    ninvoke = int(tc[-2])
    assert ncombines + nopposing + 3 + (ninvoke and 1 or 0) == len(tc)
    if not ninvoke: return []
    opposing = tc[ncombines+2:-2]
    assert all(len(o) == 2 for o in opposing)
    assert all(o[0] in ELEM and o[1] in ELEM for o in opposing)
    opposing = dict((min(o[0],o[1]), max(o[0],o[1])) for o in opposing)
    assert len(opposing) == nopposing

    invoke = tc[-1]
    assert ninvoke == len(invoke)
    assert all(e in ELEM for e in invoke)
    
    result = []
    for c in invoke:
        if len(result) > 0:
            d = result[-1]
            if c+d in combines or d+c in combines:
                del result[-1]
                c = combines.get(c+d, combines.get(d+c,None))
                assert c
        result.append(c)
        if any(x in result and opposing[x] in result for x in opposing):
            result = []
    return result
    
count = int(sys.stdin.readline())
for c,line in enumerate(sys.stdin):
    print "Case #%d: [%s]" % (c+1, ', '.join(testcase(line)))
assert c+1 == count
