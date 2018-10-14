fin = open("input.txt", 'r')
fout = open("output.txt", 'w')
T = int(fin.readline())
for cID in range(T):
    S, K = fin.readline().split()
    K = int(K)
    S = list(S)
    Flag = True
    cnt = 0
    for i in range(len(S)):
        if S[i] == '+':
            continue
        else:
            if len(S) - i >= K:
                for j in range(i, i+K):
                    if S[j] == '+':
                        S[j] = '-'
                    else:
                        S[j] = '+'
                cnt += 1
            else:
                Flag = False
                break
    r = "IMPOSSIBLE"
    if Flag:
        r = str(cnt)
    fout.write("Case #{}: {}\n".format(cID+1, r))

    