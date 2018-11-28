def func(arr, k):
    if(k==1):
        M = arr[0]
        if(M%2==0):
            return M/2, (M/2)-1
        else:
            return M/2, M/2
    else:
        M = arr[0]
        if M==1:
            io = 0
            while io<len(arr) and arr[io]==1:
                io+=1
            if(io >= k):
                return 0,0
        if(M%2==0):
            arr[0] = (M/2)-1
            arr = [M/2] + arr
        else:
            arr[0] = M/2
            arr = [M/2] + arr
        arr = sorted(arr, reverse = True)
        #print k
        return func(arr, k-1)

def func3(arr, k):
    for i in range(k,1,-1):
        M = arr[0]
        if(M%2==0):
            arr[0] = (M/2)-1
            arr = [M/2] + arr
        else:
            arr[0] = M/2
            arr = [M/2] + arr
    M = arr[0]
    if(M%2==0):
        return M/2, (M/2)-1
    else:
        return M/2, M/2

def func2(n,k):
    ans = 0.5
    l = 0
    r = 0
    while(2 * ans * k < n):
        if(r<l):
            r+=1
        else:
            l+=1
        if(ans==0.5):
            ans=1
        else:
            ans+=1
    return l,r

t = int(raw_input())
ansArr = []
for case in range(t):
    n, k = map(int, raw_input().split())
    print n,k
    arr = [n]
    ans = func(arr, k)
    ansArr.append("Case #" + str(case+1) + ": " + str(ans[0]) + " " +str(ans[1]))

f = open("../../Desktop/out.dat", "w+")

for i in ansArr:
    f.write(i + "\n")