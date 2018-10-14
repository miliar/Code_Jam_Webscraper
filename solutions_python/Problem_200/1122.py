def istidy(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    else:
        return True


for case in range(1, int(input()) + 1):
    n = input()
    tidy_n = int(n)

    while not istidy(tidy_n):
        N = [int(c) for c in str(tidy_n)]
        for i in range(len(N)):
            if any(N[i] < N[c] for c in range(0, i)):
                for z in range(i, len(N)):
                    N[z] = 9

                N[i-1] = N[i-1] - 1
                break

        tidy_n = int(''.join(str(x) for x in N))

    assert tidy_n <= int(n)
    print("Case #{}: {}".format(case, tidy_n))
