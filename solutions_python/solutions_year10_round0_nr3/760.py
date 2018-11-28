from sys import stdin

def solve():
    rounds, limit, num_groups = [int(x) for x in stdin.readline().split(" ")]
    groups = [int(x) for x in stdin.readline().split(" ")]
    profit = [0] * len(groups)
    nextes = [0] * len(groups)
    for i in xrange(len(groups)):
        total_profit = 0
        current = i
        iters = 0
        while iters < len(groups):
            if total_profit + groups[current] > limit:
                break
            total_profit += groups[current]
            current = (current + 1) % len(groups)
            iters += 1
        nextes[i] = current
        profit[i] = total_profit

    total = 0
    current = 0
    for i in xrange(rounds):
        total += profit[current]
        current = nextes[current]
    return total

cases = int(stdin.readline())
for i in xrange(cases):
    print "Case #" + str(i + 1) + ": " + str(solve())

