#!/usr/bin/env python

import sys

def b2i(b):
    base = "QWERASDF"
    return base.find(b)

def process(seq, combine, opp):
    '''
        combine = {'Q':{'A':'T'}, 'A':{'Q':'T'}}
        opp = {'Q':['S']}
    '''
    base = "QWERASDF"
    firstp = [-1 for i in xrange(len(base))]

    left = []
    basep = [-1 for i in xrange(len(base))] # first position of every base in left

    for si in xrange(len(seq)):
        s = seq[si]

        if si==0 or len(left)==0:
            left.append(s)
            continue

        last = left[-1]

        # if last element is base and could be combined with current one
        if last in combine[s]: 
            # if the combined off element is the only one, update basep
            if len(left)-1 == basep[b2i(last)]:
                basep[b2i(last)] = -1
            # update the last element
            left[-1] = combine[s][last]

        else: 
            # try to find opposed element
            clear = False
            for o in opp[s]:
                if o in left:
                    left = []
                    basep = [-1 for i in xrange(len(base))]
                    clear = True
                    continue

            if not clear: # if find no opposed
                # update basep
                if s in base and basep[b2i(s)] != -1:
                    basep[b2i(s)] = si
                left.append(s)

    return left
                

        # min = len(left)
        # # check to see if there is any opposed 
        # # update min as the first position where an opposed exists
        # for o in opp[s]:
        #     if basep[o] != -1 and basep[o] < min:
        #         min = basep[o]

        # left = left[:min]
        # # update basep 
        # for k in basep:
        #     if basep[k] >=      # update basep 
        # left = left[:min]
    
def main():
    if len(sys.argv) < 2:
        print "Usage: %s IN" % sys.argv[0]
        sys.exit(1)
    
    fin = open(sys.argv[1])
    icases = int(fin.readline().strip())

    for c in xrange(icases):
        line = fin.readline().split()
        combined = {}
        opp = {}
        
        icomb = int(line.pop(0))


        base = "QWERASDF"
        for i in base:
            combined[i] = {}
            opp[i] = []

        for i in xrange(icomb):
            comb = line.pop(0)
            c1, c2, n = list(comb)

            combined[c1][c2] = n
            combined[c2][c1] = n

        iopp = int(line.pop(0))
        for i in xrange(iopp):
            op = line.pop(0)
            c1, c2 = list(op)

            opp[c1].append(c2)
            opp[c2].append(c1)

        line.pop(0)
        seq = line.pop(0)
        ret = process(seq, combined, opp)
        l = ""
        for r in ret:
            l += (", %s" % r)
        print "Case #%d: [%s]" % (c+1, l[2:])

if __name__ == "__main__":
    main()
