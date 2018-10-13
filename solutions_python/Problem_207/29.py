def place(single, double, S, D):
    if single == double:
        return (S + D) * single, 0
    if single > double:
        return (S + D) * double + S, single - double
    if single < double:
        return "IMPOSSIBLE", -1

def greedy(n, c):
    copyn, copyc = [], []
    for i in xrange(3):
        maxn = max(n)
        index = n.index(maxn)
        copyn.append(n.pop(index))
        copyc.append(c.pop(index))
    n, c = copyn, copyc

    if (n[0] > n[1] + n[2]):
        return "IMPOSSIBLE"
    total = sum(n)
    ans = ""
    while total > 0:
        maxn = max(n)
        gg = index = n.index(maxn)

        if len(ans) > 0 and c[index] == ans[-1]:
            maxn = 0
            for i in xrange(3):
                if i != index and n[i] > maxn:
                    maxn = n[i]
                    gg = i
            if maxn == 0:
                return "IMPOSSIBLE"
        index = gg
        ans += c[index]
        n[index] -= 1
        total -= 1
    return ans;




T = int(raw_input())  
for K in xrange (T):
    n, R, O, Y, G, B, V= [int(g) for g in raw_input().split(" ")]
    s1, n1 = place(B, O, 'B', 'O')
    s2, n2 = place(Y, V, 'Y', 'V')
    s3, n3 = place(R, G, 'R', 'G')
    #print s1, n1, s2, n2, s3, n3
    if (n1 < 0 or n2 < 0 or n3 < 0 or (n1 == 0 and O + B != n and O + B != 0) or (n2 == 0 and Y + V != n and Y + V != 0) or (n3 == 0 and G + R != n and G + R != 0)): 
        ans = "IMPOSSIBLE"
    elif (n1 == n2 == n3 == 0):
        ans = s1 + s2 + s3
    else:
        ans = greedy([n1, n2, n3], ['B','Y','R'])
        if (ans != "IMPOSSIBLE"):
            #print ans
            if (O > 0):
                index = ans.index('B')
                ans = ans[:index] + s1 + ans[index + 1 :]    
            if (V > 0):
                index = ans.index('Y')
                ans = ans[:index] + s2 + ans[index + 1 :]
            if (G > 0):
                index = ans.index('R')
                ans = ans[:index] + s3 + ans[index + 1 :]
            if len(ans) > 1 and ans[0] == ans[-1]:
                ans = "IMPOSSIBLE"

    print "Case #{}: {}".format(K+1, ans)