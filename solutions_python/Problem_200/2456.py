def solve():
    N = list(int(x) for x in input())
    while True:
        i = 0
        j = None
        while i+1 < len(N):
            if N[i] > N[i+1]:
                j = i
                break
            i += 1

        if j is not None:
            N[j] -= 1
            for k in range(j+1, len(N)):
                N[k] = 9
        else:
            break

    return int(''.join(str(x) for x in N))

T = int(input())
for t in range(1, T + 1):
    print ("Case #%d: %s" % (t, solve()))
