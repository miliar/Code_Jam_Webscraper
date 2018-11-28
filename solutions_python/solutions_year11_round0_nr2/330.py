#!/usr/bin/env python
# encoding: utf-8

import sys

with open(sys.argv[1], 'r') as fin:
    with open('B-small.out', 'w') as fout:
    
        t = int(fin.readline().strip())
        
        for i in xrange(1,t+1):
            inplist = fin.readline().split()
            
            c = int(inplist[0])
            
            comb = inplist[1:c+1]
            
            d = int(inplist[c+1])
            
            oppo = inplist[c+2:c+d+2]
            
            n = int(inplist[c+d+2])
           
            invoke = inplist[c+d+3]
            
            doppo = {}
            for pair in oppo:
                if pair[0] in doppo:
                    doppo[pair[0]].append(pair[1])
                else:
                    doppo[pair[0]] = [pair[1]]
                if pair[1] in doppo:
                    doppo[pair[1]].append(pair[0])
                else:
                    doppo[pair[1]] = [pair[0]]                    
            
            dcomb = {}
            for triple in comb:
                dcomb[triple[0:2]] = triple[2]
                dcomb[triple[1]+triple[0]] = triple[2]
                
#            print doppo, dcomb, invoke
                
            out = []
            used = {}
            for letter in invoke:
                if len(out) > 0:
                    if out[-1]+letter in dcomb:
                        if used[out[-1]] == 1:
                            del used[out[-1]]
                        else:
                            used[out[-1]] -= 1
                             
                        out[-1] = dcomb[out[-1]+letter]
                        used[out[-1]] = used.get(out[-1], 0) + 1
                    elif letter in doppo:
                        for op in doppo[letter]:
                            if op in used:
                                out = []
                                used = {}
                                break
                                
                        if len(out) > 0:
                            out.append(letter)
                            used[letter] = used.get(letter, 0) + 1
                    else:        
                        out.append(letter)
                        used[letter] = used.get(letter, 0) + 1
                        
                else:
                    out.append(letter)
                    used[letter] = used.get(letter, 0) + 1
                    
            fout.write('Case #{0}: [{1}]\n'.format(i, ', '.join(out)))


