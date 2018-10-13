tcs = int(input())

for tc in range(1, tcs+1):
    n = [int(x) for x in input()]
    for c in range(len(n)-1, 0, -1):
        if n[c] < n[c-1]:
            for i in range(c, len(n)):
                n[i] = 9
            n[c-1] -= 1
    print("Case #", tc, ": ", int("".join((str(x) for x in n))), sep="")
