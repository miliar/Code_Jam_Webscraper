import sys, itertools

def partition(lst, n):
    division = len(lst) / float(n)
    return [lst[int(round(division * i)): int(round(division * (i + 1)))] for i in xrange(n)]

def get_input():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    data = []
    for line in lines[1:]:
        tokens = line.split()
        n, rest = int(tokens[0]), tokens[1:]
        data.append(partition(rest, n))
    return data

def solve(case):
    case = map(lambda x: (x[0], int(x[1])), case)
    goals = {'O': map(lambda x: x[1], filter(lambda x: x[0] == 'O', case)),
             'B': map(lambda x: x[1], filter(lambda x: x[0] == 'B', case))}
    pos = {'O': 1,
           'B': 1}

    def do(r, goal, me):
        if pos[r] == goal:
            if me:
                goals[r].pop(0)
                return True
        elif pos[r] < goal:
            pos[r] += 1
        elif pos[r] > goal:
            pos[r] -= 1
        return False

    n = 0
    for r, p in case:
        other = r == 'O' and 'B' or 'O'
        other_goal = goals[other] and goals[other][0] or None

        done = False
        while not done:
            n += 1
            done = do(r, p, True)
            if other_goal:
                do(other, other_goal, False)
    return n

data = get_input()
for idx, case in enumerate(data):
    print "Case #%s: %s" % (idx+1, solve(case))
