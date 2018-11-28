T = int(input())
for case in range(1, T+1):
    n = list(map(int, input()))
    for _ in range(len(n)):
        for i in range(1, len(n)):
            if n[i] < n[i-1]:
                for j in range(i, len(n)):
                    n[j] = 9
                n[i-1] -= 1

    result = "".join(map(str, n))
    result = int(result)
    print(f"Case #{case}: {result}")
