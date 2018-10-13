#!/usr/bin/python -tt

import sys

#base_elem = [Q, W, E, R, A, S, D, F]

def main():
    if len(sys.argv) != 2:
        print 'Requires input file'
        sys.exit()
    fname = sys.argv[1]
    fptr = open(fname, 'r')
    numtest = int(fptr.readline().split(' ')[0])
    outptr = open('output', 'w')
    
    for i in xrange(numtest):
        combinations = {}
        input = fptr.readline().split(' ')
        ptr = 0
        C = int(input[ptr])
        ptr = ptr+1
        for tmp in xrange(C):
            comb = list(input[ptr])
            #print comb
            ptr = ptr +1
            combinations[tuple(sorted([comb[0], comb[1]]))] = comb[2]
        #print combinations
        
        oppose = {}
        D = int(input[ptr])
        ptr = ptr +1
        for tmp in xrange(D):
            opp = list(input[ptr])
            ptr = ptr + 1
            if opp[0] in oppose or opp[1] in oppose:
                print 'Understanding problem statement fails'
                sys.exit(-1)
            oppose[opp[0]] = opp[1]
            oppose[opp[1]] = opp[0]
        
        N = int(input[ptr])
        ptr = ptr+1
        #print oppose
        
        orig = input[ptr]
        #print 'To invoke: ', orig
        # Magicka begins
        finlist = [orig[0]]
        for tmp in xrange(1, N):
            #print 'final list: ', finlist
            # check for clearing
            finlist.append(orig[tmp])
            # combination
            if len(finlist) > 1 and tuple(sorted([finlist[-1], finlist[-2]])) in combinations:
                #print 'combine'
                finlist.append(combinations[tuple(sorted([finlist[-1], finlist[-2]]))])
                #print finlist
                del finlist[-2]
                del finlist[-2]
                
            oppelems = [e for e in finlist if e in oppose and oppose[e] in finlist]
            if len(oppelems) > 0:
                # need to clear list
                #print 'clear'
                del finlist[:]
                
        ansstr = '[' + ', '.join(finlist) + ']'
        outptr.write('Case #%d: %s\n' % (i+1, ansstr))

    outptr.close()
    fptr.close()
        

if __name__ == '__main__':
    main()