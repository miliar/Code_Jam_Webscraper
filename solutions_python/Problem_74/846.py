indata = open('input').read()

cases = indata.strip().split('\n')

i_case = 0
ofd = open('output', 'w')
for l in cases[1:]:
    o_list = []
    b_list = []
    turn_list = []
    fields = l.split()
    num_steps = int(fields[0])
    entries = num_steps * 2
    s = 1
    while s < entries:
        if fields[s] == 'O':
            o_list.append(int(fields[s+1]))
            turn_list.append('O')
        else:
            b_list.append(int(fields[s+1]))
            turn_list.append('B')
        s = s+2

    steps = 0
    o_dir = 1
    o_index = 0
    o_cur_pos = 1

    b_dir = 1
    b_index = 0
    b_cur_pos = 1
    
    turn_index = 0
    while 1:
        o_pressed = 0
        b_pressed = 0
        done_something = 0
        if o_index < len(o_list):
            done_something = 1
            o_dir = 1
            if o_index > 0 and (o_list[o_index] - o_list[o_index-1]) < 0:
                o_dir = -1
            if o_list[o_index] == o_cur_pos and o_pressed == 0:
                if turn_list[turn_index] == 'O':
                    print "Step %s| Push button %s" % (steps+1, o_cur_pos)
                    o_pressed = 1
                    o_index += 1
            else:
                o_cur_pos += 1 * o_dir
                o_pressed = 0
                print "Step %s| Move to button %s" % (steps+1, o_cur_pos)
        else:
            o_pressed = 0

        if b_index < len(b_list):
            done_something = 1
            b_dir = 1
            if b_index > 0 and (b_list[b_index] - b_list[b_index-1]) < 0:
                b_dir = -1
            if b_list[b_index] == b_cur_pos and b_pressed == 0:
                try:
                    if turn_list[turn_index] == 'B':
                        print "Step %s|                         Push button %s" % (steps+1, b_cur_pos)
                        b_pressed = 1
                        b_index += 1
                except:
                    import pdb; pdb.set_trace()
            else:
                b_cur_pos += 1 * b_dir
                b_pressed = 0
                print "Step %s|                         Move to button %s" % (steps+1, b_cur_pos)
        else:
            b_pressed = 0

        if done_something:
            steps += 1
            if o_pressed or b_pressed:
                turn_index += 1
        else:
            break

    i_case += 1
    ofd.write('Case #%s: %s\n' % (i_case, steps))

ofd.close()
