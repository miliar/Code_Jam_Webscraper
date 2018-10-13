t = int(input())
i = 0
while i < t:
    n=int(input())
    s=str(n)
    while True:
        s = str(n)
        li=list(s)
        #print(li)
        if sorted(li) == li:
            print("Case #"+str(i+1)+": "+str(n))
            break
        else:
            n=n-1
    i+=1
