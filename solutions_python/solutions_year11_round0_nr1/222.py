#-*- encoding: utf-8 -*-
import sys

DEBUG = False

def log(a):
    if DEBUG:
        print(a)

def solve(button_sequence):
    press_seq = [x[0] for x in button_sequence]
    o_seq = [x[1] for x in button_sequence if 'O' == x[0]]
    b_seq = [x[1] for x in button_sequence if 'B' == x[0]]
    o_pos, b_pos = 1, 1
    t = 0

    while press_seq:
        t += 1
        pressed = False

        if o_seq:
            dest = o_seq[0]
            delta = dest - o_pos
            if 0 == delta:
                if not pressed and 'O' == press_seq[0]:
                    pressed = True
                    log('Orange push button %d' % dest)
                    o_seq.pop(0)
                    press_seq.pop(0)
                else:
                    log('Orange stay @ button %d' % dest)
            elif 0>delta:
                o_pos -= 1
                log('Orange move to button %d' % o_pos)
            elif 0<delta:
                o_pos += 1
                log('Orange move to button %d' % o_pos)
        else:
            log('Orange stay @ button %d' % o_pos)

        if b_seq:
            dest = b_seq[0]
            delta = dest - b_pos
            if 0 == delta:
                if not pressed and 'B' == press_seq[0]:
                    pressed = True
                    log('Blue push button %d' % dest)
                    b_seq.pop(0)
                    press_seq.pop(0)
                else:
                    log('Blue stay @ button %d' % dest)
            elif 0>delta:
                b_pos -= 1
                log('Blue move to button %d' % b_pos)
            elif 0<delta:
                b_pos += 1
                log('Blue move to button %d' % b_pos)
        else:
            log('Blue stay @ button %d' % b_pos)

        log('-----')

    return t

if '__main__' == __name__:
    T = int(sys.stdin.readline())
    for case_n in xrange(T):
        button_sequence = []
        seq = sys.stdin.readline().strip().split()
        N = int(seq[0])
        for i in xrange(1, N*2+1, 2):
            button_sequence.append((seq[i], int(seq[i+1])))

        t = solve(button_sequence)
        print('Case #%d: %d' % (case_n+1, t))
