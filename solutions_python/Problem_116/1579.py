#!/usr/bin/env python

inputs = 'A-small-attempt0.in'

lines   = [line.strip() for line in open(inputs)]
T       = int(lines[0])
numrows  = (T*4)+T
case    = 1
out = ''
mylist = []
for x in xrange(1, numrows):
    s = lines[x]
    if len(s) == 0:
        winner = None

        # cek diagonal
        d1 = [mylist[0][0],mylist[1][1],mylist[2][2],mylist[3][3]]
        d2 = [mylist[0][3],mylist[1][2],mylist[2][1],mylist[3][0]]
        
        if set(d1) in (set(['X', 'T']), set(['X'])):   
            winner = 'X won'
        elif set(d1) in (set(['O', 'T']), set(['O'])):
            winner = 'O won'
        elif set(d2) in (set(['X', 'T']), set(['X'])):   
            winner = 'X won'
        elif set(d2) in (set(['O', 'T']), set(['O'])):
            winner = 'O won'

        else:
            for i in range(0,4):
                h = mylist[i]
                v = [mylist[0][i],mylist[1][i],mylist[2][i],mylist[3][i]]
                
                # cek horizontal
                if set(h) in (set(['X', 'T']), set(['X'])):   
                    winner = 'X won'
                    break
                elif set(h) in (set(['O', 'T']), set(['O'])):
                    winner = 'O won'
                    break
        
                # cek vertical
                elif set(v) in (set(['X', 'T']), set(['X'])):   
                    winner = 'X won'
                    break
                elif set(v) in (set(['O', 'T']), set(['O'])):
                    winner = 'O won'
                    break

        if winner is None:
            allmylist = mylist[0]+mylist[1]+mylist[2]+mylist[3]
            if '.' in allmylist:
                winner = 'Game has not completed'
            else:
                winner = 'Draw'

        out += 'Case #%i: %s\n' % (case, winner)

        mylist = []
        case +=1
        continue

    mylist.append(s)

# for last list
# cek diagonal
d1 = [mylist[0][0],mylist[1][1],mylist[2][2],mylist[3][3]]
d2 = [mylist[0][3],mylist[1][2],mylist[2][1],mylist[3][0]]

if set(d1) in (set(['X', 'T']), set(['X'])):   
    winner = 'X won'
elif set(d1) in (set(['O', 'T']), set(['O'])):
    winner = 'O won'
elif set(d2) in (set(['X', 'T']), set(['X'])):   
    winner = 'X won'
elif set(d2) in (set(['O', 'T']), set(['O'])):
    winner = 'O won'

else:
    for i in range(0,4):
        h = mylist[i]
        v = [mylist[0][i],mylist[1][i],mylist[2][i],mylist[3][i]]
        
        # cek horizontal
        if set(h) in (set(['X', 'T']), set(['X'])):   
            winner = 'X won'
            break
        elif set(h) in (set(['O', 'T']), set(['O'])):
            winner = 'O won'
            break

        # cek vertical
        elif set(v) in (set(['X', 'T']), set(['X'])):   
            winner = 'X won'
            break
        elif set(v) in (set(['O', 'T']), set(['O'])):
            winner = 'O won'
            break

if winner is None:
    allmylist = mylist[0]+mylist[1]+mylist[2]+mylist[3]
    if '.' in allmylist:
        winner = 'Game has not completed'
    else:
        winner = 'Draw'

out += 'Case #%i: %s\n' % (case, winner)

with open ('output', 'w') as f: 
    f.write (out)