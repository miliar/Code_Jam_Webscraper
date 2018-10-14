import sys

f = open(sys.argv[1])
output = open(sys.argv[2], "w")
T = int(f.readline().strip())

for i in xrange(T):
    s = f.readline().strip().split(" ")
    print s
    N = int(s[0])
    
    moves = {"O": [], "B": []}
    for j in xrange(N):
        color = s[1 + (2 * j)]
        dest = int(s[2 + (2 * j)])
        action_id = j
        moves[color].append((action_id, dest))
    
    pos = {"O": 1, "B": 1}
    
    time_count = 0
    # O
    
    current_action_id = 0
    while len(moves["O"]) or len(moves["B"]):
        time_count += 1
        print moves
        
        next_action_id = None
        for c in ["O", "B"]:
            if len(moves[c]) == 0:
                continue
            (action_id, dest) = moves[c][0]
            print "Color %s, action %s, button %s, pos %s" % (c, action_id, dest, pos[c])
            if dest > pos[c]:
                print "Move to", pos[c] + 1
                pos[c] += 1
            elif dest < pos[c]:
                print "Move to", pos[c] - 1
                pos[c] -= 1
            else:
                if current_action_id == action_id:
                    print "Push", pos[c]
                    next_action_id = action_id + 1
                    del moves[c][0]
                else:
                    print "Stay at", pos[c]
        if next_action_id:
            current_action_id = next_action_id
    print time_count
    
    o = "Case #%s: %s\n" % (i + 1, time_count)
    print o,
    output.write(o)
                
    
