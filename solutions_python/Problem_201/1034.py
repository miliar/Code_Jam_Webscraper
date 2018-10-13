# import numpy as np
# import networkx as nx
# import re
import math
# from collections import Counter
# from collections import OrderedDict
# from itertools import combinations
# from itertools import permutations

def main():
    caseCount = int(input())
    for caseIdx in range(1, caseCount + 1):
        N, K = map(int, input().strip().split(' '))

        ans = solve(N, K)

        print("Case #{}: {}".format(caseIdx, ans))


def solve(N, K):
    # find s (split) s.t. 2^s <= K < 2^(s+1)
    """ example: N = 100, K = 9 """

    # stage 1: split the stalls into approximately equal partitions
    #       , which takes 2^s - 1 steps
    splitCount = int(math.log(K, 2))
    # splitCount = K.bit_length() - 1
    occupied = 2 ** splitCount - 1
    partitions = 2 ** splitCount
    """ example:
    splitCount = 3
    occupied = 7
    partitions = 8
    """

    # stage 2: occupy the remaining stalls
    toOccupy = K - occupied
    """ example: toOccupy = 2 """

    smallPartitionLength = (N - occupied) // partitions
    bigPartitionLength = smallPartitionLength + 1
    bigPartitionCount = (N - occupied) % partitions
    # smallPartitions = partitions - bigPartitions

    if toOccupy <= bigPartitionCount:
        partitionLength = bigPartitionLength
    else:
        partitionLength = smallPartitionLength

    # will occupy bigger partitions
    LS = int(math.floor((partitionLength - 1) / 2))
    RS = int(math.ceil((partitionLength - 1) / 2))

    return "{} {}".format(max(LS, RS), min(LS, RS))

if __name__ == '__main__':
    main()
