t=int(raw_input())
i=0
while i!=t:
    i=i+1
    count=0
    sh, sm=raw_input().split()
    a=int(sh)
    b=0
    for j in range (0,a+1):
        
        b=b+int(sm[j])
        #print(b)
        while b<=j:
            count=count+1
            b=b+1
        j=j+1;
    print("case#"+i+":"+count)
