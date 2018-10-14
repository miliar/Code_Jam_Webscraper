import sys

def read_problem(line):
    vals = line.split()[1:]
    steps = []
    for i in range(len(vals)/2):
        r = vals[2*i]
        b = vals[2*i+1]
        steps.append((r,int(b)))
    return steps

def find_next(start_pos, steps):
    d = {}
    for step in steps[start_pos:]:
        if step[0] not in d:
            d[step[0]] = step[1]
        if len(d) == 2:
            break
    d.setdefault('B', None)
    d.setdefault('O', None)
    return d
def check_current_bot(bot_name):
    if bot_name == 'B':
        return 'BO'
    return 'OB'

def next_move(current_pos, destination_pos):
    if current_pos < destination_pos:
        return 1
    elif current_pos > destination_pos:
        return -1
    return 0
def solve(steps):
    pos = 0
    bots = {'O':1, 'B':1}
    bots_next = find_next(pos, steps)
    active, passive = check_current_bot(steps[pos][0])
    time = 0
    while pos < len(steps):
        time += 1
        bots[passive] += next_move(bots[passive], bots_next[passive])
        if bots[active] == bots_next[active]:
            pos += 1
            if (pos < len(steps)):
                bots_next = find_next(pos, steps)
                active, passive = check_current_bot(steps[pos][0])
        else:
            bots[active] += next_move(bots[active], bots_next[active])

    return time

input_iter = iter(sys.stdin)
N=int(next(input_iter))
for i in xrange(N):
    problem = read_problem(next(input_iter))
    s = solve(problem)
    print "Case #%i: %d" % (i+1,s)
