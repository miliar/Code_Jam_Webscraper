T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    row = input().split(" ")
    S = list(row[0])
    K = int(row[1])

    c = 0
    for i in range(len(S)-K+1):
        if S[i] == '-':
            c += 1
            for j in range(K):
                if S[i+j] == '-':
                    S[i+j] = '+'
                else:
                    S[i+j] = '-'

    impossible = False
    for i in range(len(S)-K,len(S)):
        if S[i] == '-':
            impossible = True

    print("Case #{}: {}".format(t, c if not impossible else 'IMPOSSIBLE'))