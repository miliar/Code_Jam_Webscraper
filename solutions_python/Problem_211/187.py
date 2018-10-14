import decimal
t = int(raw_input())  # read a line with a single integer
for task in xrange(1, t + 1):
    N,K = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    U = decimal.Decimal(raw_input())
    P = []
    summ = U
    for s in raw_input().split(" "):
        P.append(decimal.Decimal(s))


    P.sort(reverse = True)
    i = 0
    if U != 0:
        while i < N:
            if P[i] * (N - i) <= U + sum(P[i:]):
                break
            i += 1

        newP = P[0:i]
        for j in range(i, N):
            summ += P[j]

        avg = summ / (N - i)
        for j in range(i, N):
            newP.append(avg)

        P = newP

    ans = decimal.Decimal(1)
    for p in P:
        ans *= p

    print "Case #{}: {}".format(task, ans)



