import sys
from collections import defaultdict

def invoke(elements, opposedcache, combined, opposed, base):
#    print elements, opposedcache, base
    o = None
    try:
        o = opposed[base]
    except KeyError:
        pass
    if len(elements) == 0:
        elements.append(base)
        if o != None:
            opposedcache[base] += 1
    else:
        try:
            old = elements[-1]
            c = combined[(old, base)]
            elements[-1] = c
            if opposedcache[old] > 0:
                opposedcache[old] -= 1
        except KeyError:
#            print base, o, opposedcache[o]
            if o != None and opposedcache[o] > 0:
                del elements[:]
                opposedcache.clear()
            else:
                elements.append(base)
                if o != None:
                    opposedcache[base] += 1

def case(number, spec):
#    print spec
    num_combine = int(spec.pop(0))
    combined = {}
    for ix in range(num_combine):
        s = spec.pop(0)
        combined[(s[0], s[1])] = s[2]
        combined[(s[1], s[0])] = s[2]
    num_opposed = int(spec.pop(0))
    opposed = {}
    for ix in range(num_opposed):
        s = spec.pop(0)
        opposed[s[0]] = s[1]
        opposed[s[1]] = s[0]
    num_elements = int(spec.pop(0))
    elements = spec.pop(0)
    assert(num_elements == len(elements))
    assert(len(spec) == 0)
    output = []
    opposedcache = defaultdict(int)
    for e in elements:
        invoke(output, opposedcache, combined, opposed, e)
    print "Case #%d: [%s]"%(number, ", ".join(output))

def main(lines):
    num = int(lines[0])
    for ix, line in enumerate(lines[1:]):
        case(ix+1, line.split())

if __name__=="__main__":
    main(sys.stdin.readlines())
