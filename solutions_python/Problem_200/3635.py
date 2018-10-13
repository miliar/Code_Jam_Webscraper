l = list()
def check(s, c, t) :
    if c == 0 : l.append(t); return
    for i in range(s, 10) :
        check(i, c-1, t*10+i)
for i in range(18) :
    check(1, i+1, 0)
l.append(10**20)
T = int(input())
for t in range(T) :
    n = int(input())
    for i in range(len(l) - 1 ) :
        if l[i+1] > n : break
    print("Case #", t+1, ": ", l[i],sep='')
