def hasBigger(x,y):
    if x[0]:
        return x
    else:
        if y > x[1]:
            return (True,y)
        else:
            return x         


def war(aL1, aL2):
    
    wins = 0
    for x in aL1:
        y = reduce(hasBigger, aL2, (False,x))
        if y[0]:
            aL2.remove(y[1])
        else:
            aL2.pop(0)
            wins += 1
            
    return wins   


def deceitWar(aL1, aL2):
    
    wins = 0
    
    for x in aL1:
        
        if aL2[0] > x:
            
            aL2.pop
            
        else:
            aL2.pop(0)
            wins += 1
            
    return wins            


f = 'D-large'
infile = open(f+'.in', 'r')
outfile = open(f+'.out', 'w')

state = 0
caseNo = 0

for line in infile:
    
    if state == 0:
        
        n = int(line)
        state += 1
    
    elif state == 1:
        
        r = 0
        li = []
        caseNo += 1
        state += 1
        
    elif state == 2:
        
        li.append(map(float, line.split()))
        li[r].sort()
        r += 1
        
        if r == 2:
            state = 1
            outfile.write('Case #'+repr(caseNo)+': '+repr(deceitWar(li[0],li[1][:]))+' '+repr(war(li[0],li[1][:]))+'\n')
            
            