def isTidy(s):
    t=True
    i=0
    while t and i<len(s)-1:
        if s[i]>s[i+1] :
            t=False
        else :
            i+=1
    return t
t=int(input())
for i in range(t):
    n=input()
    j=int(n)
    while j>0 :
        if isTidy(str(j)) :
            break
        else :
            j-=1
    print("case #"+str(i+1)+": "+str(j))
