import sys
from collections import deque
import random

def solve(cakes, K):
    num = 0
    flips = deque([])
    # are we currently flipped?
    flipped = False
    for idx, cake in enumerate(cakes):
        # expire the flips
        while flips and flips[0] + K <= idx:
            flips.popleft()
            flipped = not flipped

        # handle the final-flip case
        if idx + K  > len(cakes):
            target = "+"
            if flipped:
                target = "-"

            # the cake is problematic here
            if cakes[idx] != target:
                return "IMPOSSIBLE"
        else:
            # handle the general case
            if flipped:
                if cake == "+":
                    flips.append(idx)
                    num += 1
                    flipped = not flipped
            else:
                if cake == "-":
                    flips.append(idx)
                    num += 1
                    flipped = not flipped
    return str(num)

def solve_simple(cakes, K):
    num = 0
    for idx in range(len(cakes)):
        if idx + K > len(cakes):
            if cakes[idx] == "-":
                return "IMPOSSIBLE"

        elif cakes[idx] == "-":
            num += 1
            # flip
            for x in range(K):
                if cakes[idx+x] == "-":
                    cakes[idx+x] = "+"
                else:
                    cakes[idx+x] = "-"
    return str(num)

def gen_random_case():
    s1 = 1001
    s2 = random.randint(3, s1 + 1) 
    return "".join(["+" if random.randint(0, 1) == 0 else "-" for x in range(s1)]), s2

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        cakes, K = sys.stdin.readline().split()
#        cakes, K = gen_random_case()
#        print cakes, K
        cakes = list(cakes)
        K = int(K)
        s1 = solve(cakes, K)
#        s2 = solve_simple(cakes[:], K)
#        if (s1 != s2):
#            print "FAIL", s1, s2
#        else:
#            print "PASS", s1, s2

        print "Case #{}: {}".format(case+1, solve(cakes, K))
