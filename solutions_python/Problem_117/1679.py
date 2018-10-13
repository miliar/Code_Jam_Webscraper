import sys


def problem_instances(filename):
    f = open(filename)
    num_instances = int(f.readline())
    for i in range(num_instances):
        rows, cols = map(int, f.readline().split())
        lines = []
        for r in range(rows):
            lines.append(map(int, f.readline().split()))
        yield lines


def check_vertical(instance, idx, limit):
    cons = []
    col = [instance[n][idx] for n in range(len(instance))]
    for hidx, num in enumerate(col):
        if num > limit:
            return False, []
        if num < limit:
            print "Need to check whether row %i is <= %i" % (hidx, num)
            cons.append((hidx, num, check_horizontal))

    return True, cons

def check_horizontal(instance, idx, limit):
    cons = []
    for hidx, num in enumerate(instance[idx]):
        if num > limit:
            return False, []
        if num < limit:
            print "Need to check whether column %i is <= %i" % (hidx, num)
            cons.append((hidx, num, check_vertical))

    return True, cons

def solve(instance):
    constraints = [(row_idx, max(instance[row_idx]), check_horizontal)
                   for row_idx in range(len(instance))]
    constraints.extend([(col_idx,
                         max(instance[n][col_idx] for n in range(len(instance))),
                         check_vertical)
                        for col_idx in range(len(instance[0]))])
    while constraints:
        idx, limit, func = constraints.pop()
        res, cons = func(instance, idx, limit)
        if not res:
            return "NO"
        constraints.extend(cons)

    return "YES"



filename = sys.argv[1]
out = open(filename + ".out", "w")
for idx, instance in enumerate(problem_instances(filename), 1):
    print "Case %i" % idx
    out.write("Case #%i: %s\n" % (idx, solve(instance)))