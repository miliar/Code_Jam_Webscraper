
def istidy(n):
    s=str(n)
    s2="".join(sorted(s))
    return s==s2

t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    while not istidy(n):
        s=str(n)
        for j, d in enumerate(s[::-1]):
            if d!='9':
                n-=10**j
                break
    print "Case #"+str(i+1)+": "+str(n)
