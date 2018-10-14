import sys, itertools

import psyco; psyco.full()

def valid_ratio(recip, pack):
    res = [-1, -1]
    lo = (pack * 100) / (recip * 110)
    if pack * 100 >= lo * recip * 90 and pack * 100 <= lo * recip * 110:
        res[0] = lo
        
    lo += 1
    
    if pack * 100 >= lo * recip * 90 and pack * 100 <= lo * recip * 110:
        if res[0] == -1:
            res[0] = lo
        else:
            res[0] = min(res[0], lo)
    
    lo = (pack * 100) / (recip * 90)
    if pack * 100 >= lo * recip * 90 and pack * 100 <= lo * recip * 110:
        res[1] = lo
        
    lo -= 1
    
    if pack * 100 >= lo * recip * 90 and pack * 100 <= lo * recip * 110:
        if res[1] == -1:
            res[1] = lo
        else:
            res[1] = max(res[1], lo)
            
    return res
    
def inside_all_ranges(x, ranges):
    for lo, hi in ranges:
        if lo == -1 or hi == -1 or x < lo or x > hi:
            return False
            
    return True
    
def recursive_find(n, packs, indexes, y):
    if y == n:
        return [x + 1 for x in indexes]
    else:
        best = None
        scan = []
        for i in xrange(y):
            if indexes[i] >= len(packs[i]):
                return None
            scan.append(packs[i][indexes[i]])
            
        scan.append(None)
        indexes2 = list(indexes)
        for i in xrange(indexes[y], len(packs[y])):
            scan[-1] = packs[y][indexes[y]]
            seengood = False
            for lo, hi in scan:
                if inside_all_ranges(lo, scan) or inside_all_ranges(hi, scan):
                    seengood = True
                    break
        
            if seengood:
                indexes2[y] = i
                res = recursive_find(n, packs, indexes2, y + 1)
                if res is not None:
                    return res
                    
    return None
    
def find_all(n, packs):
    #print packs
    good = 0
    indexes = [0] * n
    while True:
        indexes = recursive_find(n, packs, indexes, 0)
        if indexes is None:
            return good
        else:
            good += 1
            
    # while True:
        # print indexes
        # allgood = True
        # for i in xrange(1, y+1):
            # if not allgood:
                # break
            #print i
                
        # if allgood:
            # good += 1
            # for i in xrange(len(indexes)):
                # indexes[i] += 1
                
    # return good
            

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    
    for caseno in xrange(ncases):
        n, p = [int(x) for x in f.readline().strip().split()]
        
        recip = [int(x) for x in f.readline().strip().split()]
        packs = []
        for y in xrange(n):
            t = [int(x) for x in f.readline().strip().split()]
            packs.append(filter(lambda x: x != [-1, -1], sorted([valid_ratio(recip[y], t[x]) for x in xrange(p)])))
        
        #good = 0
        good = find_all(n, packs)
                
        # for x in itertools.product(*packs):
            # seengood = False
            # for lo, hi in x:
                # if inside_all_ranges(lo, x) or inside_all_ranges(hi, x):
                    # seengood = True
                    # break
                    
            # print x, seengood
            
            # if seengood:
                # good += 1

        print "Case #%d: %d" % (caseno + 1, good)
        #print packs
        
main()