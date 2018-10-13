# -*- coding: utf-8 -*-
from collections import deque, Counter
from itertools import combinations

with file("C-small-0.in") as inp:
    with file("C-small-0.out", "w") as outp:
        n = int(inp.readline().strip())
        for i in xrange(n):
            inp.readline()
            nums = Counter(int(x) for x in inp.readline().strip().split())
            #if i > 3: continue
            nums_elems = list(nums.elements())
            subsets = list(Counter(t) for i in xrange(1, len(nums_elems)) for t in combinations(nums_elems, i))
            variants = []
            #print "subsets", subsets, list(nums.elements())
            for sean in subsets:
                patrick = nums - sean
                patrick_xor = reduce(lambda x, y: x ^ y, patrick.elements(), 0)
                sean_xor = reduce(lambda x, y: x ^ y, sean.elements(), 0)
                #print patrick, sean, patrick_xor, sean_xor
                if patrick_xor == sean_xor:
                    variants.append(sum(sean.elements()))
            if len(variants) > 0:
                result = max(variants)
            else:
                result = "NO"
            #print result
            outp.write("Case #%s: %s\n" % (i+1, result))
