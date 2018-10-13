T = int(input())

tidy = []
tappend = tidy.append

def isTidy(n):
    k = n
    md = 9
    while (k>0):
        d = k%10
        if d > md: return False
        md = d
        k //= 10
    return True

with open('B.out', 'w+') as fout:
    for t in range(T):
        N = int(input())
        print(N)
        for i in range(N, 19, -1):
            print('\t%d'%(i))
            if i in tidy: break
            if isTidy(i): 
                break
                tappend(i)
        if N <= i: i = N
        fout.write('Case #%d: %d\n'%(t+1,i))
