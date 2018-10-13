import os

f = open(os.path.expanduser("./C-large.in"))
t = int(f.readline())

def shift(l, n):
    return l[n:] + l[:n]

for i in range(t):
    v = f.readline().split(' ')
    c = int(v[0])
    s = int(v[1])
    m = []
    m.append(c)
    while(s > 0):
        s -= 1
        m.sort(reverse=True)
        k = m.pop(0)
        if(k == 0):
            break
        ls = k / 2
        rs = (k-1) / 2
        if(s==0):
            break
        else:
            if(s%2==0):
                s /= 2
                m.append(rs)
            else:
                s = s / 2 + 1
                m.append(ls)
    print ('Case #'+repr(i+1)+': '+ repr(ls) + ' ' + repr(rs))
f.close()