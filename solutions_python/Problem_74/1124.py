#!/usr/bin/python
import sys

def solve(case,moves):
    res = 0
    currloc = {'O':1,'B':1}
    
    # each loop is 1 sec
    while True:                
        if len(moves['O'])==0 and len(moves['B'])==0:
            # done
            break

        # who's turn to go to a button? who cannot push
        move = 'O'
        nopush = 'B'
        if len(moves['O'])==0:
            # only B has moves left
            move='B'
            nopush = 'O'
        elif len(moves['B'])==0:
            # only O has moves left
            move='O'
            nopush = 'B'
        else:
            # take the earliest on the original list
            move = 'O' if moves['O'][0][1]<moves['B'][0][1] else 'B'
            nopush = 'B' if move=='O' else 'O'

        # solve actions for this time step
        
        if currloc[move]==moves[move][0][0]:
            # at the correct button - push and shift
            moves[move] = moves[move][1:]
#            print move,'push'
        elif currloc[move] < moves[move][0][0]:
            # move towards the button
            currloc[move] += 1
#            print move,'loc',currloc[move]
        elif currloc[move] > moves[move][0][0]:
            # move towards the button
            currloc[move] -= 1
#            print move,'loc',currloc[move]

        if len(moves[nopush])>0 and currloc[nopush] < moves[nopush][0][0]:
            # move towards the button
            currloc[nopush] += 1
#            print nopush,'loc',currloc[nopush]
        elif len(moves[nopush])>0 and currloc[nopush] > moves[nopush][0][0]:
            # move towards the button
            currloc[nopush] -= 1
#            print nopush,'loc',currloc[nopush]
#        else:
#            # stays in place until can push
#            print nopush,'stay',currloc[nopush]
            
        # advance time
        res += 1

    print "Case #{0}: {1}".format(case,res)

data = sys.argv[1]
f = open(data)
N = -1
case = 1

for l in f:
    l.strip()
    if N<0:
        N = int(l)
    else:
        dat = l.split()
        numbutt = int(dat[0])
        dat = dat[1:]
        moves = {'O':[],'B':[]}
        i = 0
        while len(dat)>0:
            (c,b,dat) = (dat[0],dat[1],dat[2:])
            moves[c].append((int(b),i))
            i += 1
        solve(case,moves)
        case += 1

f.close()    
