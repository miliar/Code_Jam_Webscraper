from sys import stdin


def answer(c):
    c = c[:-1]
    if len(c)==1 :
        return c
    else:
        a=''
        i=0
        j=1
        k=2
        go = True
        while go:
            if j == len(c):
                return c
            elif c[i]<c[j]:
                i=j
                j=k
                k+=1
                #if k == len(c):
                #    return c
            elif c[i]==c[j]:
                if k==len(c):
                    return c
                elif c[j]==c[k]:
                    j=k
                    k+=1
                    if k == len(c):
                        return c
                elif c[j]<c[k]:
                    i=k
                    j=k+1
                    k+=1
                else:
                    go = False
            else:
                go = False
        for j in range(0,i):
            a+=c[j]
        a+=str(int(c[i])-1)
        for j in range(i+1,len(c)):
            a+='9'
        return str(int(a))


T=int(stdin.readline())
for case in range(1,T+1):
	c=stdin.readline()
	print('Case #%i: %s' % (case,answer(c)))

