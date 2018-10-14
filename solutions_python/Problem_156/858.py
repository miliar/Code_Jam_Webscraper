def SplitNum(from_v, to_v):
    if to_v == 0:
        return 0
    count = 0
    numbers = from_v / to_v
    if from_v % to_v != 0:
        numbers += 1
    while numbers >= 2:
        v = numbers / 2
        count += v
        if numbers % 2:
            numbers = v + 1
        else:
            numbers = v
    return count


def Cost(values, x):
    total_cost = 0
    for v in values:
        if v > x:
            total_cost += SplitNum(v, x)
    return total_cost + x


def SmallestX(values, begin, end):
    min_cost = 4294967296
    for v in xrange(begin, end + 1):
        cost = Cost(values, v)
        if cost < min_cost:
            min_cost = cost
    return min_cost


def FindSolution(values):
    v0 = SmallestX(values, 1, max(values))
    v1 = Cost(values, 1)
    v2 = Cost(values, max(values))
    if v0 > 0:
        return min(v0, v1, v2)
    return min(v1, v2)


output_file = open('./pancake.out', 'w')
with open('./B-large.in', 'r') as f: 
    curr_case = 0
    for i, line in enumerate(f):
        if i == 0: continue
        if i % 2 > 0:
            curr_case += 1
        else:
            values = [int(x) for x in line.strip().split()]
            output_file.write('Case #%d: %d\n' % (curr_case, FindSolution(values)))

