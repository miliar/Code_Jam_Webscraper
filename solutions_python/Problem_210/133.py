__author__ = 'snv'

f = open('B-small-attempt0.in','r')
g = open('output.txt', 'w')
T = int(f.readline())
for j in range(T):
    N, K = f.readline().split()
    N, K = int(N), int(K)
    acts = []
    for k in range (N+K):
        acts.append(list(map(int, f.readline().split())))
    # print(acts)
    ans = 2
    if (N*K == 0) and (N+K) == 2:
        acts = sorted(acts)
        # print(acts)
        if (acts[1][1] - acts[0][0] > 720) and (acts[1][0] - acts[0][1] < 720):
            ans = 4

    ans_string = 'Case #{0}: {1}\n'.format(j+1, ans)
    print(ans_string)
    g.write(ans_string)
f.close()
g.close()

