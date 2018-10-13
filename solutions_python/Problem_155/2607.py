def standingOvation (sMax,shyString):
    
    cume = 0
    n = 0
    aNeeded = 0
    
    for s in shyString:
        aNeeded = max(n - cume,aNeeded) #Determines how many additional audience members re needed to make this group stand
        cume = cume + int(s)
        n = n+1

    return aNeeded


        
f = open('A-large.in','r')
o = open('standingOvationLarge.txt','w')
T = int(f.readline())

for i in range(1,T+1):
    Line = f.readline().split()
    o.write('Case #'+ repr(i) + ': '+repr(standingOvation(Line[0],Line[1]))+'\n')
    
f.close()
o.close()
    


