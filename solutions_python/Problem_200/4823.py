
T = int(input().strip())

def isTidy(num):
    
    ch = str(num)
    
    for i in range(len(ch)-1):

        if(int(ch[i]) > int(ch[i+1])):
            return False
    return True

for i in range(T):
    N = int(input().strip())
    
    while(not isTidy(N)):
        N = N - 1
    print("Case #"+str(i+1)+": ", N)
          