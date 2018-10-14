def solve():
    s, k = input().split()
    k = int(k)
    state = [1 if it == '+' else 0 for it in s]
    cost = 0
    for i in range(len(state) - (k - 1)):
        if(state[i] == 0):
            cost += 1
            for j in range(k):
                state[j+i] ^= 1
        if all(state):
            print("Case #{}: {}".format(case, cost))
            return
    print("Case #{}: IMPOSSIBLE".format(case))


numCases = int(input())
for case in range(1, numCases + 1):
    solve()
