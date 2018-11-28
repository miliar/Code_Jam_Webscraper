n = int(input())
for i in range(n):
    p,s =(input().split(" "))
    p,s = [list(p),int(s)]
    c =0
    f =0
    for j in range(len(p)):
        if (p[j]=="-"):
            c  = c+1
            for k in range(s):
                if j+k<len(p):
                    if p[j+k]=="-":
                        p[j+k]="+"
                    else:
                        p[j+k]="-"
                elif(f==0):
                    print("Case #{}: IMPOSSIBLE".format(i+1))
                    f =f+1            
    if(f==0):
        print("Case #{}: {}".format(i+1,c))
    
