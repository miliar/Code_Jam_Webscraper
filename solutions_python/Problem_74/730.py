import sys

if len(sys.argv) < 2:
    print "correct usage: python bot_trust.py <filename>"
    sys.exit()

f = open(sys.argv[1], 'r')
line = f.readline()
pos = {}
pot={}
orange = False
blue = True
count = 1
while line:
    line = f.readline()
    pos[orange] = 1
    pot[orange] = 0
    pos[blue] = 1
    pot[blue] = 0
    time = 0
    ord = line.split()[1:]
    if len(ord) < 1: continue
    ix = 0
    last_move = None
    while ix < len(ord):
        move = (ord[ix] == "B")
#        print "moving now", ord[ix]
#        print "blue", pos[blue], pot[blue]
#        print "orange", pos[orange], pot[orange]
#        print "time", time
        new_pos = int(ord[ix+1])
        if move is last_move:
            diff = abs(pos[move]-new_pos) + 1
            time += diff
            pos[move] = new_pos
            pot[not move] += diff
        else:
            diff = max(abs(pos[move]-new_pos) - pot[move],0) + 1
            pos[move] = new_pos
            pot[move] = 0
            time += diff
            pot[not move] = diff
        last_move = move
        ix+=2
    print "Case #%d:"%count,time
    count+=1
