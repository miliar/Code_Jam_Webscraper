from __future__ import division
'''
'''

file = open('in.txt','r')
out = open('out.txt','w')
test_cases = file.readlines()

def compute(X,R,C):
    '''
    if it is possible to cover
    '''
    A = R * C
    if X > R and X > C: return False
    if A % X != 0: return False
    
    if R == 1 or C == 1:
        if X > 2: return False
        else: return True
        
    if R == 2 or C == 2:
        if X <= 2: return True
        elif X == 3:
            if A < 6: return False
            else: return True
        elif X == 4:
            # add #4 of X=4, then 'thunder'
            return False 
    
    if R == 3 or C == 3: return True
    if R == 4 or C == 4: return True
    
    return True

lineId = 1
caseId = 0
while lineId < len(test_cases):
    caseId += 1
    (X,R,C) = tuple(map(lambda x:int(x),test_cases[lineId].strip().split(' ')))
    
    state = compute(X,R,C)
    
    answer = 'GABRIEL' if state == True else 'RICHARD'
    print >> out, "Case #%d: %s" % (caseId,answer)
    lineId += 1

file.close()
out.close()