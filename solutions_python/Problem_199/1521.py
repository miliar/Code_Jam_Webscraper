T = int(input())
lines = []
for _ in range(T):
    lines.append(input().split(" "))

for case, line in enumerate(lines):
    K = int(line[1])
    S = list(line[0])
    length = len(S)
    i = 0
    counter = 0
    while i + K <= length:
        if S[i] == "+":
            i += 1
        elif S[i] == "-":
            for j in range(K):
                S[i + j] = "+" if S[i + j] == "-" else "-"
            counter += 1
            i += 1
    while i < length:
        if S[i] == "-":
            break
        i += 1
    else:
        print("Case #{}: {}".format(case + 1, counter))
        continue
    print("Case #{}: IMPOSSIBLE".format(case + 1))
