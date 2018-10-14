import itertools

d = {0: [[0, 0, 0]], 1: [[0, 0, 1]], 2: [[0, 0, 2], [0, 1, 1]], 3: [[0, 1, 2], [1, 1, 1]], 4: [[0, 2, 2], [1, 1, 2]], 5: [[1, 1, 3], [1, 2, 2]], 6: [[1, 2, 3], [2, 2, 2]], 7: [[1, 3, 3], [2, 2, 3]], 8: [[2, 2, 4], [2, 3, 3]], 9: [[2, 3, 4], [3, 3, 3]], 10: [[2, 4, 4], [3, 3, 4]], 11: [[3, 3, 5], [3, 4, 4]], 12: [[3, 4, 5], [4, 4, 4]], 13: [[3, 5, 5], [4, 4, 5]], 14: [[4, 4, 6], [4, 5, 5]], 15: [[4, 5, 6], [5, 5, 5]], 16: [[4, 6, 6], [5, 5, 6]], 17: [[5, 5, 7], [5, 6, 6]], 18: [[5, 6, 7], [6, 6, 6]], 19: [[5, 7, 7], [6, 6, 7]], 20: [[6, 6, 8], [6, 7, 7]], 21: [[6, 7, 8], [7, 7, 7]], 22: [[6, 8, 8], [7, 7, 8]], 23: [[7, 7, 9], [7, 8, 8]], 24: [[7, 8, 9], [8, 8, 8]], 25: [[7, 9, 9], [8, 8, 9]], 26: [[8, 8, 10], [8, 9, 9]], 27: [[8, 9, 10], [9, 9, 9]], 28: [[8, 10, 10], [9, 9, 10]], 29: [[9, 10, 10]], 30: [[10, 10, 10]]}

t = int(raw_input())

for i in range(t):
    line = raw_input()
    tokens = line.split()
    n = int(tokens[0])
    s = int(tokens[1])
    p = int(tokens[2])
    best = 0

    scores = [int(tokens[3+j]) for j in range(n)]
    scores_to_compare = [d[j] for j in scores]
    cartesian_product = [j for j in itertools.product(*scores_to_compare)]

    for product in cartesian_product:
        count_best = 0
        count_s = 0
        for score in product:
            if score[2] - score[0] == 2:
                count_s += 1
            if score[2] >= p:
                count_best += 1
        if count_s == s and count_best > best:
            best = count_best

    print "Case #" + str(i+1) + ": " + str(best)
