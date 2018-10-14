'''
Created on May 6, 2011

@author: mogox
'''

import math
dbg=False
outfilename= 'a-small.out'
outfile = open(outfilename, 'w+')

def log(s):
    if dbg:
        print s
    
def write(s):
    print s
    outfile.write(s+"\n")
        
def calculateMovingTime(start,btn):
    return math.fabs(btn-start)

#        0 1 2 3 4 5 6 7 8
#Case -> 4 O 2 B 1 B 2 O 4
def SolveCase(t, data):
    case=data.split(' ')
    time=0
    op=int(case[0])
    Opos=1
    Bpos=1
    freeTurns=0
    IsOLastAction=False
    IsBLastAction=False
    IsOAction=False
    m=0
    i=1
    while i <len(case):
        if i%2==0:
            btn=int(case[i])
            if IsOAction:
                log('Moving O from '+str(Opos) + 'To ' +str(btn) + ' - Time:'+str(time)+ ' Free: '+str(freeTurns))
                m=calculateMovingTime(Opos, btn)
                Opos=btn
                if IsBLastAction:
                    if m >= freeTurns:
                        m=m-freeTurns
                        freeTurns=m+1
                    else:
                        freeTurns=1
                        m=0
                else:
                    freeTurns+=m+1
                IsOLastAction= True
                IsBLastAction = False
                time+=(m+1)
            else:
                log('Moving B from '+str(Bpos) + 'To ' +str(btn) + ' - Time:'+str(time)+ ' Free: '+str(freeTurns))
                m=calculateMovingTime(Bpos, btn)
                Bpos=btn
                if IsOLastAction:
                    if m >= freeTurns:
                        m=m-freeTurns
                        freeTurns=m+1
                    else:
                        freeTurns=1
                        m=0
                else:
                    freeTurns+=m+1
                IsOLastAction = False
                IsBLastAction = True
                time+=(m+1)
        else:
            IsOAction=case[i]=='O'
        i+=1        
     
        
    write('Case #'+str(t)+': '+str(int(time)))


ts=raw_input()
t=int(ts)
for case in range(0,t):
    data=raw_input()
    SolveCase(case+1, data)