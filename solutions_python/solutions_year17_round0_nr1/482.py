N = int(input())
for n in range(N):
    config, K = input().split()
    config = [c for c in config]
    K = int(K)
    step = 0
    for i in range(len(config)-1, -1, -1):
        if config[i] == "-":
            if i < K-1:
                step = -1
                break
            else:
                for j in range(i - K+1, i+1):
                    config[j] = '+' if config[j] == '-' else '-'
                step += 1
    print("Case #", n+1, ": ", "IMPOSSIBLE" if step == -1 else step, sep = "")
