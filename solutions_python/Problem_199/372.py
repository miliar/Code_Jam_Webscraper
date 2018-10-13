T = int(input())
for case in range(1, T+1):
    pan, k = input().split()
    pan = list(map(lambda x: x == "-", pan))
    k = int(k)
    result = 0
    for i, p in enumerate(pan):
        if p:
            if k + i > len(pan):
                result = "IMPOSSIBLE"
                break
            result += 1
            for j in range(k):
                pan[j+i] = not pan[j+i]
    print(f"Case #{case}: {result}")
