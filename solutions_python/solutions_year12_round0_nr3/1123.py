import numpy as np
T = int(raw_input())

def cycle(seq):
    new = seq[1:]
    new.append(seq[0])
    return new

for c in range(T):
    distinct = []
    case = "Case #%d:" % (c+1)
    
    A,B = np.array(raw_input().split(), dtype=int)
    n = A
    o = len(str(A))
    
    pairs = 0
    while n!=B:
        cyc = list(str(n))

        # construct all cycles
        perms = []
        for i in range(o):
            cyc=cycle(cyc)            
            ncyc = int(''.join(cyc))
            if len(str(ncyc))==o: perms.append(ncyc)
            
        # construct all pairs
        for i in range(len(perms)):
            for j in range(i+1,len(perms)):
                pa = perms[i]
                pb = perms[j]
                
                ps=[(pa,pb), (pb,pa)] # not sure if this matters, just to ensure every combination checked                
                #if pa<pb:   pair=(pa,pb)
                #else:       pair=(pb,pa)            
                for pair in ps:                
                    if A<=pair[0] and pair[0] < pair[1] and pair[1]<=B:                
                        if not pair in distinct:
                            distinct.append(pair)
                            #print A,"<=",pair[0],"<",pair[1],"<=",B
                            pairs+=1
            
        n+=1
    
    print "%s %d" % (case, pairs)
            
            
            