import numpy as np
T = int(raw_input())

for c in range(T):
    case = "Case #%d:" % (c+1)
    data = raw_input().split()
    N = np.array(data[0], dtype=int)    # number of Googlers
    S = np.array(data[1], dtype=int)    # number of surprises
    p = np.array(data[2], dtype=int)    # best score
    t = np.array(data[3:], dtype=int)   # total scores
    
    bests = 0
    
    s = []
    for score in t:
        # see if naturally best or need surprise result    
        split = int(score/3.0)
        rem = score%3
        if (rem==0): 
            if split >= p: bests+=1     # natural split is best
            elif (split-1)>=0 and (split+1)>= p and S>0: # can 'borrow' but will be surprise
                S-=1
                bests+=1
        elif (rem==1): # natural only, borrowing doesnt help
            if split>=p or (split+1)>=p: bests+=1
        elif (rem==2): # can use surprise            
            if split >= p: bests+=1      # naturally best on lowest
            elif (split+1)>=p: bests+=1  # naturally best on separated by one split
            elif S>0 and (split+2)>=p:   # if we can have a surprise win then use one
                S-=1
                bests+=1
    
    print "%s %d" % (case, bests)
            
            
            