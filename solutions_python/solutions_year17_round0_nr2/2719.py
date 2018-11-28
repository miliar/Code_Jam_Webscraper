# -*- coding: utf-8 -*-
t = int(input())
f = open("output.txt", 'w', encoding="utf-8")
for k in range(1, t + 1):
    m = int(input())
    l = list(map(int, str(m)))
    if sorted(l) == l:
        f.write("Case #{}: {}\n".format(k, m))
    else:
        l = len(str(m))
        p = []
        for i in range(l):
            l1 = ['9']*l
            for j in range(i+1):
                l1[j] = str(str(m)[j])
            ind = i
            if l1[ind] == '0':
                continue
            while int(''.join(l1)) > m and ind < len(str(int(''.join(l1)))):
                if l1[ind] == '0': ind += 1
                else: l1[ind] = str(int(l1[ind])-1)
            p.append(int(''.join(l1)))
        p = sorted(p, reverse=True)
        for i in p:
            t = list(map(int, str(i)))
            if t == sorted(t):
                f.write("Case #{}: {}\n".format(k, i))
                break
f.close()
