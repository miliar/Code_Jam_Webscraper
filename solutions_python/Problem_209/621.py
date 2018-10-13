from itertools import combinations
pi = 3.14159265358979323846
def calc(a,b):
    return ((a[0]**2) - (b[0]**2)) + 2*(a[0]*a[1])
    
for t in range(input()):
    n,k = map(int,raw_input().strip().split())
    arr = []
    for a in range(n):
        arr.append(map(int,raw_input().strip().split()))
    if k==1 or n==1:
        temp = map(lambda x: (x[0]**2) + 2*x[0]*x[1],arr)
        #print temp
        ans = pi*max(temp)
    else:
        ans = 0
        for i in combinations(arr,k):
            #print i
            tempa = 0
            i = sorted(i,key= lambda x:x[0],reverse = True)
            for j in range(k-1):
                tempa += calc(i[j],i[j+1])
            ans = max(pi*(tempa+i[k-1][0]**2+2*i[k-1][0]*i[k-1][1]),ans)
            
    print "Case #{}: {}".format(t+1,ans)