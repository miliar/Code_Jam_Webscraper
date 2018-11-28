infile = open('A-small-attempt0.in', 'r')
outfile = open('A-small-attempt0.out', 'w')

state = 0
caseNo = 0

for line in infile:
    
    if state == 0:
        
        n = int(line)
        state += 1
    
    elif state == 1:
        
        li = []
        caseNo += 1
        r = 0
        r1 = int(line)
        state += 1
        
    elif state == 2:
        
        r += 1
        if r == r1:
            li1 = map(int, line.split())
        if r == 4:
            state += 1            
    
    elif state == 3:
        
        r = 0
        r2 = int(line)
        state += 1    
        
    elif state == 4:
        
        r += 1
        if r == r2:
            
            li2 = map(int, line.split())
            
            for x in li1:
                for y in li2:
                    if x == y:
                        li.append(x)
            
            if len(li) > 1:
                outfile.write('Case #'+repr(caseNo)+': Bad magician!\n')
            elif len(li) == 0:   
                outfile.write('Case #'+repr(caseNo)+': Volunteer cheated!\n') 
            elif len(li) == 1:
                outfile.write('Case #'+repr(caseNo)+': '+repr(li[0])+'\n')        
            
        if r == 4:
            state = 1            
        
        
        