t = int(input())
for i in range(1,t+1):
    s, k = input().split(' ')
    k = int(k)
    f = list(s)
    c = 0
    pre = [s]
    im = False
    while len([x for x in s.split('+') if x != '']) != 0:
        for j in range(0,len(f)-k+1):
            if f[j] == '-':
                for p in range(j,j+k):
                    if f[p] == '+':
                        f[p] = '-'
                    else:
                        f[p] = '+'
                c += 1
        s = ''.join(f)
        if s in pre:
            im = True
            break
        else:
            pre.append(s)
    if im:
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i,c))
