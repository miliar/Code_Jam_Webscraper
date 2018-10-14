import sys

def prebottrust(line):
    N = int( line[0] )
    seq = line[1:]
    seq_actor = [ seq[i*2] for i in range(len(seq)/2) ]
    seq_button = [ int(seq[i*2+1]) for i in range(len(seq)/2) ]
    return bottrust( seq_actor, seq_button )

def bottrust( seq_actor, seq_button ):
    idle = {'O':0, 'B':0}
    position = {'O':1, 'B':1}
    time = 0
    for a in range( len(seq_actor) ):
        actor = seq_actor[a]
        button = seq_button[a]
        btime = 1 + max(0, abs(position[actor]-button)-idle[actor] )
        position[actor] = button
        idle[actor] = 0
        if actor == 'B':
            idle['O'] += btime
        else:
            idle['B'] += btime
        time += btime
    return time

T = int( sys.stdin.readline().strip() )

for i in range(T):
    line = sys.stdin.readline().strip()
    line = line.split(" ")
    print "Case #%s: %s" % (i+1, prebottrust(line))

