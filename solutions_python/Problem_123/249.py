#fi=open("A-small-attempt0.in",'r')#Input File
#fo=open("A-small-attempt0.out",'w')#Output File

fi=open("A-large.in",'r')#Input File
fo=open("A-large.out","w")#Output File

#fi=open("A.in",'r')#Input File
#fo=open("A.out","w")#Output File

def find(arr, a, n, i):
    ans = 0
    
    while i<n and arr[i] < a:
        a += arr[i]
        i += 1
        
    if i<n:
        while arr[i] >= a:
            a += a - 1
            ans += 1
            if ans > (n-i):
                return n-i
        ans += find(arr, a, n, i)

        if ans > (n-i):
            ans = n-i
    return ans   
       
T=int(fi.readline())
for case in range(1,T+1,1):
    ans = 0
    ############################################
    a, n = map(int, fi.readline().split())
    arr = map(int, fi.readline().split())
    arr.sort()
    ans = find(arr, a, n, 0)
    ############################################
    fo.write("Case #%s: %s\n"%(case, ans))
