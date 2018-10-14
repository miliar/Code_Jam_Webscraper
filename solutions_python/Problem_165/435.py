t=int(input())
m=0
while m<t:
    m+=1
    a=input()
    s=0
    r,c,w=[int(n) for n in a.split()]
    s=(r-1)*(c-2*(w-1))+int((c/w)+w-0.001)
    print("Case #%s: %s"%(m,s))
              
