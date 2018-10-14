import sys
VERBOSE = 0
def resolve(seq, o_seq, b_seq):
    if VERBOSE:
        print '-' * 20
        print seq
        print o_seq
        print b_seq
    total_time = 0
    o_current_position = 1
    b_current_position = 1
    try:
        o_next_position = o_seq.pop(0)
    except IndexError:
        o_next_position = -1
    try:
        b_next_position = b_seq.pop(0)
    except IndexError:
        b_next_position = -1
    while seq:
        next = seq.pop(0)
        robot = next[0]
        button = int(next[1:])
        if VERBOSE:
            print '*' * 10
            print 'time: %d' %total_time
            print 'robot O:\n cp: %d, np: %d' % (o_current_position, o_next_position)
            print 'robot B:\n cp: %d, np: %d' % (b_current_position, b_next_position)
            print 'robot %s in action' %robot
            print '*' * 10
        if robot == 'O':
            o_time = abs(o_next_position - o_current_position) + 1
            total_time += o_time
            o_current_position = button
            try:
                o_next_position = o_seq.pop(0)
            except IndexError:
                o_next_position = -1
            #now calc b_current_position
            if b_next_position == -1:
                continue
            #forward travelling
            if b_next_position >= b_current_position:
                diff = b_next_position - b_current_position - o_time
                if diff < 0:
                    b_current_position = b_next_position
                else:
                    b_current_position = b_current_position + o_time
            #backward travelling
            else:
                diff = b_current_position - b_next_position - o_time
                if diff < 0:
                    b_current_position = b_next_position
                else:
                    b_current_position = b_current_position - o_time
        elif robot == 'B':
            b_time = abs(b_next_position - b_current_position) + 1
            total_time += b_time
            b_current_position = button
            try:
                b_next_position = b_seq.pop(0)
            except IndexError:
                b_next_position = -1
            #now calc o_current_position
            if o_next_position == -1:
                continue
            #forward travelling
            if o_next_position >= o_current_position:
                diff = o_next_position - o_current_position - b_time
                if diff < 0:
                    o_current_position = o_next_position
                else:
                    o_current_position = o_current_position + b_time
            #backward travelling
            else:
                diff = o_current_position - o_next_position - b_time
                if diff < 0:
                    o_current_position = o_next_position
                else:
                    o_current_position = o_current_position - b_time
    return total_time
    
def main():
    file = open(sys.argv[1])
    length = file.readline()
    case_num = 1
    for line in file.readlines():
        ll = line.split(' ')
        N = int(ll[0])
        seq = []
        o_seq = []
        b_seq = []
        for i in xrange(1, N*2, 2):
            robot = ll[i]
            button = ll[i+1]
            seq.append(robot + button)
            if robot == 'O':
                o_seq.append(int(button))
            elif robot == 'B':
                b_seq.append(int(button))
        result = resolve(seq, o_seq, b_seq)
        print 'Case #%d: %s' %(case_num, result) 
        case_num += 1

if __name__ == '__main__':
    main()
