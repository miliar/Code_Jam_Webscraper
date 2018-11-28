
if __name__=='__main__':
    T = int(input())
    
    for i in range(1,T+1):
        [A,B,K] = [int(x) for x in input().rstrip().split(' ')]
        ans = 0
        for x in range(A):
            for y in range(B):
                if x&y < K:
                    ans+=1
        tp = 'Case #'+str(i)+': '+str(ans)
        print(tp)
        
