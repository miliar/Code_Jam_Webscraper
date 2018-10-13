import sys

test_cases = int(sys.stdin.readline())

def solve_test_case(num):
    ints = [int(x) for x in str(sys.stdin.readline()).split()]
    num_googlers = ints[0]
    surprising_triplets = ints[1]
    limit = ints[2]
    scores = ints[3:]
    sure = 0
    doubtful = 0
    for s in scores:
        if s == 0:
            if limit <= 0:
                sure += 1
            continue
        if s%3 == 0:
            if s/3 >= limit:
                sure += 1
            elif s/3 + 1 >= limit:
                doubtful += 1
        if s%3 == 1:
            if s/3 + 1 >= limit:
                sure += 1
        if s%3 == 2:
            if s/3 + 1 >= limit:
                sure += 1
            elif s/3 + 2 >= limit:
                doubtful += 1
    result = sure + min(surprising_triplets, doubtful)
    print "Case #" + str(num) + ": " + str(result)

for i in range(test_cases):
    solve_test_case(i+1)
