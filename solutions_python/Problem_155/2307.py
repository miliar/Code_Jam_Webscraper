def solve(S):
    S = [int(x) for x in S]
    n = len(S)
    flow = [0]
    j = 1
    res = 0
    for i in xrange(0, n):
        if flow[j - 1] >= i:
            flow.append(flow[j - 1] + S[i])
        if flow[j - 1] < i:
            new_friends = i - flow[j - 1]
            res += new_friends
            flow.append(flow[j - 1]  + S[i] + new_friends)
        j += 1
    return res

f = open('A1.in', 'r')
input = [l.strip() for l in f.readlines()]
f.close()

T = int(input[0])
for t in xrange(1, T + 1):
    Smax, S = input[t].split()
    print 'Case #{t}: {res}'.format(t=t, res=solve(S))
