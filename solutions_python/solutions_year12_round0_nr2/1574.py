t = int(input())
for i in range(t):
    numbers = list(map(int,input().split()))
    n, s, p, sums = numbers[0], numbers[1], numbers[2], numbers[3:]
    unconditional = 0
    conditional = 0
    for j in range(n):
        if sums[j] >= p*3-2:
            unconditional += 1
        elif sums[j] >= p*3-(4 if p > 1 else 2):
            conditional += 1
    print("Case #%d: %d" % (i+1, unconditional + min(conditional, s)))
