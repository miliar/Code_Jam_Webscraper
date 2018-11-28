#!/usr/bin/env python
import sys

BOT_NAMES = ['O', 'B']

class InputException(Exception):
    pass

def parse_file(filename):
    f = file(filename, 'r')
    case_num = int(f.readline())
    cases = f.readlines()
    if len(cases) != case_num:
        raise InputException("bad input: case number mismatch")
    f.close()
    return [parse_case_input(case) for case in cases]

def parse_case_input(case):
    moves = case.strip().split()
    num_moves = int(moves[0])
    moves = moves[1:]
    if (len(moves) % 2 == 1) or (num_moves != len(moves) / 2):
        raise InputException("bad input: bad case input", case)
    
    ret = []
    for i in xrange(0, len(moves), 2):
        ret.append((moves[i], int(moves[i + 1])))
        if not ret[-1][0] in BOT_NAMES:
            raise InputException("bad input: unrecognized move", move)
    
    return ret

def get_next_button(sequence, bot):
    for next_move in sequence:
        if next_move[0] == bot:
            return next_move[1]

def solve_case(sequence):
    sequence_idx = 0
    num_moves = 0
    states = {}
    #get first command
    for bot in BOT_NAMES:            
        # get new command 
        states[bot] = [1, get_next_button(sequence, bot)]
        
    next_button = False
    while sequence_idx < len(sequence):
        num_moves += 1
        for bot, state in states.iteritems():            
            if state[1] is None:
                # do nothing
                pass
            elif state[1] == state[0]:
                # reached button, press it if its the bot turn
                if sequence[sequence_idx][0] == bot:
                    next_button = True
                    state[1] = get_next_button(sequence[sequence_idx + 1:], bot)
                # otherwise wait
            else:
                if state[1] > state[0]:
                    state[0] += 1 # move forward
                else:
                    state[0] -= 1 # move backwards
        
        if next_button:
            sequence_idx += 1
            next_button = False

    return num_moves 

def main():
    if len(sys.argv) != 3:
        print 'usage: %s <inputfile> <outputfile>' % sys.argv[0]
        return
    
    try:
        cases = parse_file(sys.argv[1])
    except InputException, e:
        print 'Got exception:', e
        return
    
    sys.stdout = file(sys.argv[2], 'w')
    
    for count in xrange(len(cases)):
        print 'Case #%d: %d' % (count + 1, solve_case(cases[count]))
         
if __name__=='__main__':
    main()
    
        
