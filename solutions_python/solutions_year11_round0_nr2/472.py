import collections
import sys

inp = sys.stdin

T = int(inp.readline())
for i, line in enumerate(inp, 1):
    split = line.split()
    C = int(split.pop(0))
    combiners = [split.pop(0) for _ in xrange(C)]
    D = int(split.pop(0))
    destructors = [split.pop(0) for _ in xrange(D)]
    N = int(split.pop(0))
    invoke_list = list(split.pop(0))

    element_list = []
    for invoked in invoke_list:
        element_list.append(invoked)
        if len(element_list) <= 1:
            continue

        combined = False
        last_pair = tuple(element_list[-2:])
        for b1, b2, e in combiners:
            if last_pair == (b1, b2) or \
               last_pair == (b2, b1):
                element_list.pop()
                element_list[-1] = e
                combined = True
                break
        if not combined:
            assert len(element_list) >= 2
            last_elem = element_list[-1]
            for e1, e2 in destructors:
                if last_elem not in (e1, e2):
                    continue
                if (last_elem == e1 and e2 in element_list) or \
                   (last_elem == e2 and e1 in element_list):
                    element_list = []
                    break
    print 'Case #%d: [%s]' % (i, ', '.join(element_list))
    
