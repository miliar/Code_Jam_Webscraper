import sys

num_cases = int(sys.stdin.readline())

def get_steps(n, seq):
    count = 0
    prev_dur = 0
    this_dur = 0
    O_pos = B_pos = 1
    cur_robot = seq[0]
    i = 0
    while i < len(seq):
        robot = seq[i]
        new_pos = int(seq[i+1])
        old_pos = O_pos if robot == 'O' else B_pos
        if robot != cur_robot:
            count += this_dur
            prev_dur = this_dur
            this_dur = 0
            cur_robot = robot
            delta_dist = new_pos - old_pos
            if delta_dist < 0:
                old_pos -= min(prev_dur, abs(delta_dist))
            else:
                old_pos += min(prev_dur, delta_dist)
        delta_dist = new_pos - old_pos
        this_dur += abs(delta_dist) + 1
        if robot == 'O':
            O_pos = new_pos
        else:
            B_pos = new_pos
        i += 2
    return count + this_dur


for j in xrange(num_cases):
    test = sys.stdin.readline().split()
    N = int(test[0])
    if N != len(test) / 2:
        raise Exception("input format error")
        
    print "Case #%s: %s" % (j+1, get_steps(test[0], test[1:]))
    j += 1
