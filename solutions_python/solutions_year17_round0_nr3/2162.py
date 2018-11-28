import sys
import math
from heapq import *
from functools import lru_cache
from collections import Counter


def allocate_one_stall(empty_range):
    # Person will sit directly in the middle of the empty space
    # If there are two equidistant seats they will pick the left-most one
    pos = math.floor(empty_range / 2)
    # Calculate the distances
    Ls = math.floor(empty_range / 2)
    Rs = empty_range - math.floor(empty_range / 2) - 1
    # Return the maximum and minimum distances
    return max(Ls, Rs), min(Ls, Rs)


# @lru_cache()
def allocate_stalls(empty_range, k):
    """
    Returns the values of max(Ls, Rs) and min(Ls, Rs) such that all k people have been allocated stalls
    Does it recursively in naive fashion
    """

    # Base case: only one person to allocate
    if k == 1:
        return allocate_one_stall(empty_range)

    # Recursive case
    # This person will sit in the middle,
    # so the next person must be seated in one half of the now bifurcated empty range
    # Find what the max/min values will be recursively
    leftMax, leftMin = allocate_stalls(math.floor(empty_range / 2), k - 1)
    rightMax, rightMin = allocate_stalls(empty_range - math.floor(empty_range / 2) - 1, k - 1)

    # If one has better min value than the other, that will be used, otherwise compare on their max values
    if leftMin > rightMin:
        return leftMax, leftMin
    elif rightMin > leftMin:
        return rightMax, rightMin
    else:
        # Compare on the mins, if they're the same then return the leftmost (not that it matters)
        if rightMax > leftMax:
            return rightMax, rightMin
        else:
            return leftMax, leftMin


def bruteforce_stalls(n, k):
    state = [False] * (n + 2)
    state[0] = True
    state[-1] = True

    allocateVals = None

    while k > 0:
        values = []
        # Calculate values for all stalls
        for i in range(1, n + 1):
            if not state[i]:
                # Stalls to the left
                j = i - 1
                Ls = 0
                while not state[j]:
                    Ls += 1
                    j -= 1
                # Stalls to the right
                j = i + 1
                Rs = 0
                while not state[j]:
                    Rs += 1
                    j += 1
                # Push the calculated values as a heap
                heappush(values, (-min(Ls, Rs), -max(Ls, Rs), i))
        # Retrieve the maximum from the heap (which will be the leftmost one if there are duplicates)
        allocateVals = heappop(values)
        state[allocateVals[2]] = True
        k -= 1

    return -allocateVals[1], -allocateVals[0]







def solve(n: int, k: int):
    return bruteforce_stalls(n, k)

#################################
# Parse input and solve


def run():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    results = []
    with open(input_file, 'r') as f:
        num_cases = int(f.readline())
        for i in range(0, num_cases):
            case_str = f.readline()
            n = int(case_str.split(' ')[0])
            k = int(case_str.split(' ')[1])

            (rl, rr) = solve(n, k)
            results.append('Case #{0}: {1} {2}\n'.format((i + 1), rl, rr))
            print('Solved {0}/{1}'.format((i + 1), num_cases))

    with open(output_file, 'w') as f:
        f.writelines(results)

    print('[Complete]')

if __name__ == '__main__':
    run()
