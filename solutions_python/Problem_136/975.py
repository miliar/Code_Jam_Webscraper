def fastestTime(aC, aF, aX):
    
    rate = 2    
    time = 0
    
    while (aC/rate)+(aX/(rate+aF)) < (aX/rate):
        time += aC/rate
        rate += aF
         
    time += aX/rate
    
    return time


f = 'B-large'
infile = open(f+'.in', 'r')
outfile = open(f+'.out', 'w')

state = 0
caseNo = 0

for line in infile:
    
    if state == 0:
        
        n = int(line)
        state += 1
    
    elif state == 1:
        
        caseNo += 1
        li = map(float, line.split())
        t = fastestTime(li[0],li[1],li[2])
        outfile.write('Case #'+repr(caseNo)+': '+repr(round(t,7))+'\n')
        