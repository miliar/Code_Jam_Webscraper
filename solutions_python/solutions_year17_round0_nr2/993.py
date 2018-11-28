from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    N = stdin.readline().strip()
    ok = False
    while not ok:
        prev = 0
        for i in range(len(N)):
            if int(N[i]) < prev:
                M = int(N[:i]) - 1
                N = (str(M) if M != 0 else '') + ('9' * len(N[i:]))
                break
            prev = int(N[i])
        else:
            ok = True
    stdout.write("Case #{:d}: {:s}\n".format(case_num, N))
