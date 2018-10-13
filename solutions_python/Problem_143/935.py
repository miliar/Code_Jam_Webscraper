def solve(f):
    a, b, k = tuple([int(s) for s in f.readline().split()])
    answer = a * b
    big, small = max(a, b), min(a, b)

    max_big_bit = 0
    big_copy = big >> 1
    while big_copy != 0:
        max_big_bit += 1
        big_copy = big_copy >> 1

    max_small_bit = 0
    small_copy = small >> 1
    while small_copy != 0:
        max_small_bit += 1
        small_copy = small_copy >> 1

    near_max = 0
    for bad in range(k, small + 1):
        for bit in range(max_bit+1):
            pass

def solve_one(f):
    answer = 0
    a, b, k = tuple([int(s) for s in f.readline().split()])
    for i in range(a):
        for j in range(b):
            if (i & j) < k:
                answer += 1
    return answer

import sys
f = open(sys.argv[1], "r")
num_tests = int(f.readline())
for i in range(num_tests):
    print "Case #" + str(i+1) + ": " + str(solve_one(f))
