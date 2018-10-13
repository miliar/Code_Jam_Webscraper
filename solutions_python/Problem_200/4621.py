t = int(input())

def check_tidy(N):
    while(True):
        tt = True
        l = str(N)
        if(len(l) == 1):
            return N
        else:
            for i in range(0,len(l)-1):
                if(int(l[i+1])<int(l[i])):
                    tt = False
            if(tt == False):
                N= N-1
            else:
                return(N)
                    
                
        

    
for i in range(0,t):
    N = int(input())

    n = check_tidy(N)

    print("Case #{}: {}".format((i+1),n))
