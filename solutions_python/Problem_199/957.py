from sys import stdin, stdout

T = int(stdin.readline().strip())

for case_num in range(1, T+1):
    S,K = stdin.readline().strip().split()
    S = list(S)
    K = int(K)

    flips = 0
    for i in range(len(S) - K + 1):
        if S[i] == '-':
            flips += 1
            for j in range(K):
                S[i+j] = '+' if S[i+j] == '-' else '-'
        if all(map(lambda x: x=='+', S)):
            break
    if all(map(lambda x: x=='+', S)):
        stdout.write("Case #{:d}: {:d}\n".format(case_num, flips))
    else:
        stdout.write("Case #{:d}: IMPOSSIBLE\n".format(case_num))
