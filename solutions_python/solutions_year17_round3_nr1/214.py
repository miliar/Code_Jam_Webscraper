import math
import decimal
pi = math.pi
def getArea(cakes):
    cakes = sorted(cakes, key = lambda x:x[0], reverse = True)
    answer = decimal.Decimal(pi * float(cakes[0][0]) * float(cakes[0][0]))
    for cake in cakes:
        answer += decimal.Decimal(2.0 * pi * float(cake[0]) * float(cake[1]))
    return answer

t = int(raw_input())  # read a line with a single integer
for task in xrange(1, t + 1):
    N,K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    cakes = []
    for i in range(0, N):
        cakes.append([int(s) for s in raw_input().split(" ")])

    new_cakes = sorted(cakes, key = lambda x:x[0])

    picks = new_cakes[0:K]

    for i in range(K, N):
        cake = new_cakes[i]
        max_diff = cake[0] * cake[1] - picks[0][0] * picks[0][1]
        max_idx = 0
        for j in range(1, K):
            diff = cake[0] * cake[1] - picks[j][0] * picks[j][1]
            if diff > max_diff:
                max_diff = diff
                max_idx = j
        if i == N - 1:
            if cake[0] * cake[0] - picks[K-1][0] * picks[K-1][0] + 2 * max_diff > 0:
                picks.remove(picks[max_idx])
                picks.append(cake)
        elif max_diff > 0:
            picks.remove(picks[max_idx])
            picks.append(cake)

#    print picks
    answer = getArea(picks)
    print "Case #{}: {}".format(task, answer)




