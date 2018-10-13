
T=int(input())

for i in range(T):
    l=input().split()
    a=int(l[0])
    b=int(l[1])
    c=int(l[2])
    c*=3
    tab=[]
    for j in range(a):
        tab.append(int(l[j+3]))
    tab.sort()
    tab.reverse()
    r=0
    j=0
    while j<len(tab) and tab[j]>=(c-2) and (tab[j]>0 or c<=0):
        r+=1
        j+=1
    while j<len(tab) and tab[j]>=(c-4) and b>0 and (tab[j]>1 or c<=1):
        r+=1
        j+=1
        b-=1
    print("Case #"+str(i+1)+": "+str(r))
