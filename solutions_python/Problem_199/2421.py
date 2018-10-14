def flip(pancakes, i, K):
    for j in range(i, i + K):
        pancakes[j] = not pancakes[j]

for t in range(int(input())):
    answer = 'IMPOSSIBLE'

    S, K = input().split()
    K = int(K)

    pancakes = [p == '+' for p in S]

    count = 0
    for i in range(len(S) - K + 1):
        if not pancakes[i]:
            flip(pancakes, i, K)
            count += 1

    if all(pancakes):
        answer = count

    print("Case #{}: {}".format(t + 1, answer))

