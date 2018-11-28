def otoc(pac, od, k):
    for i in range(od, od+k):
        pac[i] = 1-pac[i]

def plusminus(pac, od, k):
    plus, minus = 0, 0
    for i in range(od, od+k):
        if pac[i] == 0:
            minus += 1
        else:
            plus += 1
    return (plus, minus)

def dasa(pac, od, k):
    if od+k == len(pac):
        pl, mi = plusminus(pac, od, k)
        if pl == k:
            return 0
        if mi == k:
            return 1
        return 10047
    if pac[od] == 1:
        return dasa(pac, od+1, k)
    otoc(pac, od, k)
    return 1+dasa(pac, od+1, k)

T = int(input())
for t in range(1, T+1):
    s, k = input().split()
    k = int(k)
    pac = [0 if x=='-' else 1 for x in s]
    print("Case #%d: " % t, end="")
    res = dasa(pac, 0, k)
    if res >= 10047:
        print("IMPOSSIBLE")
    else:
        print(res)
