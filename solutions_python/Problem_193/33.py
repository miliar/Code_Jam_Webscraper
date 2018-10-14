from collections import deque
from copy import deepcopy

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    work = [list(map(int, input())) for _ in range(n)]
    know = [set([i for i in range(n) if work[j][i]]) for j in range(n)]
    depart = [set([i]) for i in range(n)]
    # print(know)
    for i in range(n):
        for j in range(n):
            if know[i] & know[j]:
                know[i] |= know[j]
                know[j] = know[i]
                depart[i] |= depart[j]
                depart[j] = depart[i]
    result = 0
    solo = 0
    aband = 0
    for i in range(n):
        result += len(know[i]) - sum(work[i])
        if len(depart[i]) == 1:
            solo += 1
        for j in range(n):
            if work[j][i]:
                break
        else:
            depart.append(set())
            know.append(set([i]))

    visited = [0] * n
    for i in range(n-1, -1, -1):
        if len(depart[i]):
            m = min(depart[i])
            if visited[m]:
                del know[i]
                del depart[i]
                continue
            visited[m] = 1
        if len(know[i]) == len(depart[i]):
            del know[i]
            del depart[i]
    if len(know):

        def is_corr(kn, dp):
            for i in range(len(kn)):
                if len(kn[i]) != len(dp[i]):
                    return False
            return True

        q = deque([[know, depart, 0]])
        cost = float("inf")
        while len(q):
            kno, dep, cos = q.pop()
            if cos > cost:
                continue
            m = len(kno)
            for i in range(m):
                for j in range(i+1, m):
                    kn, dp = deepcopy(kno), deepcopy(dep)
                    co = cos + len(dp[i]) * len(kn[j] - kn[i]) + len(dp[j]) * len(kn[i] - kn[j])
                    # print(co)
                    if co > cost:
                        continue
                    kn[i] |= kn[j]
                    dp[i] |= dp[j]
                    del kn[j]
                    del dp[j]
                    if is_corr(kn, dp):
                        # print("Zmaga", kn, dp)
                        cost = min(co, cost)
                    else:
                        q.append([kn, dp, co])

        result += cost
        # print(know)
        # print(depart)
    print("Case #{}: {}".format(case, result))
