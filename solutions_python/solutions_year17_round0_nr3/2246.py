# Python 3.5

# Algorithm
# Let's define each state as (a1, a2, ..., an)
# Each ai means the number of empty stalls between occupied stalls
# Therefore, for (a1, a2, ..., an), (n-1) stalls are occupied
# At a entrance of person, (a1, a2, ..., an) becomes (a1, a2, ..., a(n+1))
# with following rule
# 1. Find the largest ai. If there are multiple of them, choose the leftmost one.
# 2. For such ai,
#   a) min(Ls, Rs) = max(Ls, Rs) = (ai-1)/2 for odd ai
#   b) min(Ls, Rs) = (ai-2)/2, max(Ls, Rs) = ai/2 for even ai
# 3. Replace ai with min(Ls, Rs), max(Ls, Rs). Now we have (n+1) terms in state
# This works since if both min(Ls, Rs) and max(Ls, Rs) is maximal,
# ai would be the maximal.
#     Time: O(n^2)

# Another one
# For N=500, the size of gap that people select are
# 250, 249, 125, 124, 124, 124, 62, 62, 62, 62, 62, 61, 61, 61, ...
# and we can observe that
# K=1: 500/1 = 500 ... 0 => 500
# K=2-3: (500-1)/2 = 249 ... 1 => 250, 249
# K=4-7: (500-3)/4 = 124 ... 1 => 125, 124, 124, 124
# K=8-15: (500-7)/8 = 61 ... 5 => 62, 62, 62, 62, 62, 61, 61, 61
#     Time: O(1)

import math

def main():
    problem = open("C-small-2-attempt0.in", "r")
    output = open("C-out.txt", "w")

    test_case = int(problem.readline().strip())

    for test in range(test_case):
        line = problem.readline().strip().split()
        N = int(line[0])
        K = int(line[1])
        logK = int(math.log(K, 2))
        max_power_2 = 2 ** logK
        q = int((N - max_power_2 + 1)/max_power_2)
        r = (N - max_power_2 + 1) - q * max_power_2
        if (K - max_power_2) < r:
            selected_gap = q+1
        else:
            selected_gap = q
        if selected_gap % 2 == 0:
            max_lsrs = int(selected_gap/2)
            min_lsrs = max_lsrs - 1
        else:
            max_lsrs = int((selected_gap-1)/2)
            min_lsrs = max_lsrs
        output.write("Case #" + str(test+1) + ": " + str(max_lsrs) + " " + str(min_lsrs) + "\n")
    problem.close()
    output.close()

main()
    
