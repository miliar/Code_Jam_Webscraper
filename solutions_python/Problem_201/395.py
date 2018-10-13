import sys
import math

with open(sys.argv[1]) as infile:
    input = infile.readlines()

T = int(input[0])

result = []


def split_one_space(s):
    s2 = (s - 1) // 2
    s1 = s - 1 - s2
    return [s1, s2]


def split_spaces(n1o, n2o, s1o, s2o):
    s2 = (s2o - 1) // 2
    s1 = s2 + 1
    if s2o % 2 == 1:  # Smaller s is even
        n2 = 2 * n2o + n1o
        n1 = n1o
    else:
        n2 = n2o
        n1 = 2 * n1o + n2o
    return n1, n2, s1, s2


def solve_stalls(N, K):

    # full_splits = int(math.log2(K))

    # spaces = 2 ** full_splits

    # space_len = (N - (spaces - 1)) / spaces
    # s2 = int(space_len)
    # s1 = s1 + 1

    # spaces // s1


    # if K == 1
    #     return split_one_space(N)

    k = 0
    for i in range(N):  # Not going all the way ever
        if i == 0:
            n1, n2, s1, s2 = 1, 0, N, (N - 1)
        else:
            n1, n2, s1, s2 = split_spaces(n1, n2, s1, s2)
        # print (i)
        # print (n1, n2, s1, s2)
        new_k = k + 2**i
        if new_k < K:
            k = new_k
            continue
        # else now going to finish
        # print ('final')
        K_left = K - k
        # print (K_left)
        if K_left <= n1:
            return split_one_space(s1)
        else:
            return split_one_space(s2)


for line in input[1:]:
    N, K = (int(s) for s in line.split()[:2])
    result.append(solve_stalls(N, K))

with open(sys.argv[1].split('.')[0] + '.out', 'w') as outfile:
    for i, r in enumerate(result):
        outfile.write("Case #%s: %s %s\n" % (i + 1, r[0], r[1]))
