import sys

def process_game(a, motes):
    motes.sort()
    while len(motes) > 0 and motes[0] < a:
        #print '+' + str(motes[0]) + " ",
        a += motes.pop(0)
        
    if len(motes) != 0:
        mote_added = list(motes)
        mote_added.append(a - 1)
        mote_rmvd = motes[:len(motes) - 1]
        if a == 1:
            return len(motes)
        return 1 + min(process_game(a, mote_added), process_game(a, mote_rmvd)) 
        
    return 0


f = open(sys.argv[1], 'r')
f.readline()
line = f.readline()
case = 1
while line:
    a = int(line.split(' ')[0])
    motes = map(int, f.readline().split(' '))
    moves = process_game(a, motes)
    
    print 'Case #' + str(case) + ': ' + str(moves)
    case += 1
    line = f.readline()