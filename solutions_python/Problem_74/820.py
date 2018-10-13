#!/usr/bin.python

def bot(steps, op = 1, bp = 1):
    if steps == []:
        return 0

    time_taken = 0
    next_stop = int(steps[1])

    if steps[0] == 'O':
        next_to_next_stop = get_next_stop('B', steps[2:])
        time_taken = time_taken + abs(op - next_stop) + 1
        op = next_stop
        if next_to_next_stop:
            bp = bring_closer(bp, next_to_next_stop, time_taken)
    else:
        next_to_next_stop = get_next_stop('O', steps[2:])
        time_taken = time_taken + abs(bp - next_stop) + 1
        bp = next_stop
        if next_to_next_stop:
            op = bring_closer(op, next_to_next_stop, time_taken)

    return time_taken + bot(steps[2:], op, bp)

def get_next_stop(color, steps):
    if steps == []:
        return None
    if steps[0] == color:
        return int(steps[1])

    return get_next_stop(color, steps[2:])

def bring_closer(cp, np, time_taken):
    if cp > np:
        if time_taken >= abs(cp - np):
            return np
        else:
            return cp - time_taken
    else:
        if time_taken >= abs(cp - np):
            return np
        else:
            return cp + time_taken

if __name__ == '__main__':
    test_cases = int(raw_input())
    for i in range(1, test_cases + 1):
        steps = raw_input().split()
        print 'Case #' + str(i) + ': ' + str(bot(steps[1:]))

