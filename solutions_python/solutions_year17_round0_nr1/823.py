for _ in range(int(input())):
    s, k = input().split()
    k = int(k)
    l = [c=='+' for c in s]
    cc = 0
    for i in range(len(l)-k+1):
        if not l[i]:
            cc += 1
            for x in range(k):
                l[i+x] = not l[i+x]
    print('Case #%s: %s' % (_+1, cc if all(l) else 'IMPOSSIBLE'))
        
    