import sys

def direction(start, end):
    diff = end - start
    
    if (diff != 0):
        return diff / abs(diff)
    else:
        return 0

input = sys.stdin
cases = int(input.readline())

for case in xrange (cases):
    info = input.readline().strip().split(" ")
    
    buttons = int(info[0])

    seconds = 0
    
    orange_pos = 1
    blue_pos = 1
    
    orange_moves = []
    blue_moves = []
        
    moves = []
    for i in range(buttons):
        robot = info[1 + i * 2]
        position = int(info[2 + i * 2])
        moves.append(robot)
        
        if (robot == 'O'):
            orange_moves.append((position, i))
        else:
            blue_moves.append((position, i))
            
    orange_target = 0
    blue_target = 0
    who_push = 0
    done = False
    
    orange_done = False
    blue_done = False
    
    while not done:
        orange_moved = False
        if not orange_done and len(orange_moves) > 0: 
            orange_dest = orange_moves[orange_target][0]
            orange_move = direction(orange_pos, orange_dest)
            orange_pos += orange_move
            if (orange_move != 0):
                orange_moved = True

        blue_moved = False
        if not blue_done and len(blue_moves) > 0:        
            blue_dest = blue_moves[blue_target][0]
            blue_move = direction(blue_pos, blue_dest)
            blue_pos += blue_move
            if (blue_move != 0):
                blue_moved = True
        
        if (who_push < len(moves) and moves[who_push] == 'O'):
            if (orange_pos == orange_dest and not orange_moved):
                orange_target += 1
                
                if (orange_target == len(orange_moves)):
                    orange_done = True
                    
                who_push += 1
        else:
            if (blue_pos == blue_dest and not blue_moved):
                blue_target += 1
                
                if (blue_target == len(blue_moves)):
                    blue_done = True
                    
                who_push += 1
            
        seconds += 1
        
        if (who_push == buttons):
            done = True

    print "Case #%d: %d" % (case + 1, seconds)
