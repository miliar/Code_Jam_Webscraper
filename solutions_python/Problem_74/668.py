import sys

lines = sys.stdin.readlines()
lines = map(lambda a:a.rstrip('\n'), lines)
#print lines

N = int(lines[0])
for i in range(N):
    data = lines[i+1].split()
    T = int(data[0])
    #print T,data
    
    colors = []
    o_positions = []
    b_positions = []
    for j in range(T):
        color = data[j*2+1]
        pos = data[j*2+2]
        if color=='O':
            colors.append('O')
            o_positions.append(pos)
        else:
            colors.append('B')
            b_positions.append(pos)
    
    def flag(i):
        if i==0:
            return 0
        if i>0:
            return 1
        if i<0:
            return -1
    
    o_pos = 1
    b_pos = 1
    step = 0
    o_active = True
    b_active = True
    for j in range(T):
        color = colors[j]
        
        # target O
        if len(o_positions)==0:
            o_active = False
        else:
            o_next = int(o_positions[0])
            if color=='O':
                o_positions = o_positions[1:]
        # target B
        if len(b_positions)==0:
            b_active = False
        else:
            b_next = int(b_positions[0])
            if color=='B':
                b_positions = b_positions[1:]
        
        # temp_move O
        o_move = 0
        if o_active and o_pos!=o_next:
            o_move = o_next - o_pos
        # temp_move B
        b_move = 0
        if b_active and b_pos!=b_next:
            b_move = b_next - b_pos
        
        #print 'o', o_next, o_move
        #print 'b', b_next, b_move
        
        # move
        if color=='O':
            if abs(o_move)<abs(b_move): # b long
                step += abs(o_move)
                o_pos = o_next
                if b_active:
                    b_pos += flag(b_move)*abs(o_move)
            else: # o long
                step += abs(o_move)
                o_pos = o_next
                if b_active:
                    b_pos = b_next
        else: # color='B'
            if abs(o_move)<abs(b_move): # b long
                step += abs(b_move)
                b_pos = b_next
                if o_active:
                    o_pos = o_next
            else: # o long
                step += abs(b_move)
                b_pos = b_next
                if o_active:
                    o_pos += flag(o_move)*abs(b_move)
        
        # push
        step += 1
        if color=='O' and b_pos!=b_next:
            b_pos += flag(b_next-b_pos)
        if color=='B' and o_pos!=o_next:
            o_pos += flag(o_next-o_pos)
            
        #print j, step, o_pos, b_pos, o_active, b_active
    print 'Case #%d: %d' % (i+1, step)
        
        