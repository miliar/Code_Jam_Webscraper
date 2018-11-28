t = int(input())

def inv(a):
    if a == '-':
        return '+'
    else:
        return '-'

for T in range(t):
    cont = 0
    s, k = input().split()
    v = [s[i] for i in range(len(s))]
    k = int(k)
    n = len(s)
    i = 0
    while i < n: 
        if v[i] == '-' and i+k <= n:
            cont += 1
            for j in range(i,i+k):
                v[j] = inv(v[j])
        elif v[i] =='-':
            cont = -1
            break
        i+=1

    if cont != -1:
        print("Case #%d: %d" % (T+1, cont))
    else:
        print("Case #%d: IMPOSSIBLE" % (T+1))
