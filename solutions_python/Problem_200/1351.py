import sys

def tidy(N):
    result=int(N[-1])

    dd=10
    p = result
    for i in range(-1,-len(N),-1):
        q = int(N[i-1])
        #print (q, p)

        if (q>p):
            result=q*dd-1
            p=q-1
        else:
            result+=q*dd
            p=q
        dd*=10

    return result

if __name__=='__main__':
    T = int(sys.stdin.readline())
    for i in range(T):
        N=sys.stdin.readline().rstrip()
        print("Case #%d: %d" % (i+1,tidy(N)))

