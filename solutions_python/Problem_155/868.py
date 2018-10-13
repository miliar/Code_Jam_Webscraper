import sys

def solve_case(line):
    highest_sl, str = line.split(' ')
    highest_sl = int(highest_sl)
    ppl = [int(x) for x in str]

    running_sum = 0
    need_to_add = 0

    for sl, count in enumerate(ppl):
        if running_sum < sl and count > 0:
            to_invite = sl - running_sum
            need_to_add += to_invite
            running_sum += to_invite
        running_sum += count

    return need_to_add


lines = sys.stdin.readlines()

testcases = int(lines[0])

lines = lines[1:]
lines = [l.rstrip() for l in lines]

results = []

for i in range(testcases):
    results.append(solve_case(lines[i]))

for i, r in enumerate(results, start = 1):
    print ("Case #%d: %d" % (i, r))

