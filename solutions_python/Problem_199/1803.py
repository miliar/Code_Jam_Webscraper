import sys
# print("Case #{}: {} {}".format(i, n + m, n * m))

sys.stdin  = open("a.in")
sys.stdout = open("ao.out","w")



def changer(s,i,t) :
    for it in range(i,i+t):
        if(s[it]=='+') :
            s[it]='-'
        else :
            s[it]='+'
    
    return s

n = int(input())
for i in range(n) :
    line = input().split(' ')
    possible = True
    out = 0
    line[0] = list(line[0])
    
    while (possible):
        
        try :
            ind = int(line[0].index('-'))
            if (ind + int(line[1]) <= len(line[0])):
                line[0]=changer(line[0],ind,int(line[1]))
                out = out + 1
            else :
                possible = False
                out = -1            
        except :
            possible = False        
        
        #print(line[0])
    print("Case #",i+1,":",sep='',end=' ')
    
    if out==-1:
        print("IMPOSSIBLE")
    else :
        print(out)