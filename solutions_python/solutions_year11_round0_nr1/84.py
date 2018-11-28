
def read_ints():
    return map(int, raw_input().split(" "))



T, = read_ints()
for cas in range(T):
    mvs = raw_input().split(" ")
    
    b_pos = 1
    o_pos = 1
    b_time = 0
    o_time = 0
    cur_time = 0
    for i in range(1, len(mvs), 2):
        #print mvs[i], mvs[i+1]
        who = mvs[i]
        pos = int(mvs[i+1])
        
        if who == 'O':
            start_pos = o_pos
            start_time = o_time
        else:
            start_pos = b_pos
            start_time = b_time
        
        move_cost = abs(start_pos - pos)
        t = 0
        if move_cost + start_time <= cur_time:
            t = cur_time + 1
        else:
            t = move_cost + start_time + 1

        if who == 'O':
            o_pos = pos
            o_time = t
        else:
            b_pos = pos
            b_time = t
        cur_time = max(b_time, o_time, t)

        #print "i = %d" % i
        #print "B %s %d" % (b_pos, b_time)
        #print "O %s %d" % (o_pos, o_time)
        #print 
        
    print "Case #%d: %d" % (cas+1, cur_time)
