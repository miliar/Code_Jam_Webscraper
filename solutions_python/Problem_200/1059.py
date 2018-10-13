# import numpy as np
# import networkx as nx
# import re
# import math
# from collections import Counter
# from collections import OrderedDict
# from itertools import combinations
# from itertools import permutations

def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        # read an integer
        N = int(input())

        ans = solve(N)

        print("Case #{}: {}".format(caseIdx, ans))

def solve(N):
    digits = list(map(int, str(N)))

    for i in range(len(digits) - 1):
        # find the first digit that digits[i] > digits[i+1]
        if digits[i] > digits[i+1]:
            # set the digits after i+1 to 9
            for j in range(i+1, len(digits)):
                digits[j] = 9

            # digits[i] -= 1
            for j in range(i, -1, -1):  # [i, ..., 1, 0]
                if digits[j] != 0:
                    digits[j] -= 1
                    # if digits[j-1] >= digits[j], need to keep processing
                    if j > 0 and digits[j-1] > digits[j]:
                        digits[j] = 9
                        continue
                    else:
                        break
                else:
                    digits[j] = 9

    return int(''.join(map(str,digits)))

if __name__ == '__main__':
    main()
