import sys
from itertools import tee

it = iter(sys.stdin.readlines())
it.next() # Burn the number of tests

def set_or_append(d, key, item):
    try:
        d[key].append(item)
    except KeyError:
        d[key] = [item]

case = 1
while(True): 
    try:
        items = iter(it.next().split())
    except StopIteration:
        break
    items, items2 = tee(items,2)
    num_comb = int(items.next())
    combinations = {} #{letter:[list of other letter, replacement tuples]}
    for _ in range(num_comb):
        c = items.next()
        set_or_append(combinations, key=c[0], item=(c[1], c[2]))
        set_or_append(combinations, key=c[1], item=(c[0], c[2]))
    num_opp = int(items.next())
    opposed = {}
    for _ in range(num_opp):
        o = items.next()
        set_or_append(opposed, key=o[0], item=o[1])
        set_or_append(opposed, key=o[1], item=o[0])
    items.next() # Burn num elements
    elements = items.next()
    #print ', '.join(items2)
    
    # Check items
    out = []
    #print "Elements: %s   Comb: %s   Opposed: %s" % (elements, combinations, opposed)
    for e in elements:
        #print "%s - Looking at %s" % (out, e)
        if len(out) == 0:
            out.append(e)
            continue
        
        done = False
        # Check for combinations  
        c = combinations.get(e, [])
        for other, replacement in c:
            #print "Combination for %s checking if last letter is %s" % (e, other)
            if other == out[-1]:
                out.pop()
                out.append(replacement)
                #print "Matched: %s. Out now %s" % (replacement, out)
                done = True
                break
        if done:
            continue
                
        # Check for opposed
        o = opposed.get(e, [])
        for other in o:
            #print "Opposed for key %s, checking for any match of %s" % (e, other)
            if other in out:
                out = []
                #print "Opposed %s. Zeroing list." % o
                done = True
                break
        if done:
            continue
        
        out.append(e)
        
    print "Case #%s: %s" % (case, '['+', '.join(out)+']')
    case += 1