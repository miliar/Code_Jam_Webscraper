import math

def getNum():
    inp = input()
    return int(inp)

def getArrNum():
    inp = input()
    A = [int(x) for x in inp.split(' ')]
    return A
    
if __name__=='__main__':
    T = getNum()
    for t in range(T):
        ans = "Case #"+str(t+1)+": "
        arr = getArrNum()
        N = arr[0]
        K = arr[1]
        lst = []
        for n in range(N):
            arr = getArrNum()
            R = arr[0]
            H = arr[1]
            lst.append((math.pi*R*R,2*math.pi*R*H))
        lst.sort(reverse=True)
        val = 0.0
        for k in range(N-K+1):
            tval = lst[k][0] + lst[k][1]
            nl = [lst[x][1] for x in range(k+1,N)]
            nl.sort(reverse=True)
##            print(k)
##            print(nl)
##            print(tval)
            for x in range(K-1):
                tval += nl[x]
            val = max(val,tval)
        ans += str(val)
        print(ans)
            
                
            
            
            
            
        
        



    
