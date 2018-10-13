t=input()
for i in range(int(t)):
    
    n=list(input())
    #int_n=int(str("".join(n)))
    if len(n)!=1:
        for j in range(len(n)-1):
            for k in range(len(n)-1):
                if int(n[k])>int(n[k+1]) or n[k+1]=='0' or n[k]=='0':
                    if int(n[k])>0:
                        n[k] = str(int(n[k])-1)
                    for l in range(k+1,len(n)):
                        n[l] = '9'
                
        #for p in range(int(s),
    s = "".join(n)      
    print("Case #"+str(i+1)+": " + str(int(s)))