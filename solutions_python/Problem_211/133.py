import sys
import math
from decimal import *

def solve(units, core_probs):
    core_probs = sorted(core_probs)
    num_in_set = 1
    ind = 0
    current = core_probs[0]
    cur_val = 0
    while ind < len(core_probs):
        if ind == len(core_probs) - 1:
            current += (units / num_in_set)
            break
        else:
            needed_val = num_in_set * (core_probs[ind+1] - current)
            if units >= needed_val:
                units -= needed_val
                num_in_set += 1
                current = core_probs[ind+1]
            else:
                current += Decimal(units) / Decimal(num_in_set)
                break
        ind += 1
    cur_val = Decimal(0)
    cur_val = Decimal(math.pow(current, num_in_set))
    index = ind + 1
    while index < len(core_probs):
        cur_val *= core_probs[index]
        index += 1
    return cur_val


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        N, K = map(int, sys.stdin.readline().split())
        U = Decimal(sys.stdin.readline())
        cores = sys.stdin.readline().split()
        cores = [Decimal(x) for x in cores]
        print "Case #{}: {}".format(case + 1, format(solve(U, cores), '.8f'))
