numberTestCases = input()
for t in range(1, numberTestCases + 1):
    p, k = raw_input().split()
    p = list(p)
    k = eval(k)
    flips = 0
    isHappy = True

    for i in range(len(p) - k + 1):
        if (p[i] is "-"):
            flips += 1
            for j in range(k):
                p[i + j] = "+" if p[i + j] is "-" else "-"

    for i in range(len(p) - k, len(p)):
        if p[i] is "-":
            isHappy = False
            break

    if isHappy:
        print("Case #{0}: {1}".format(t, flips))
    else:
        print("Case #{0}: IMPOSSIBLE".format(t))
