def split(num):
    nums=[]
    while(num>0):
       nums.append(num%10)
       num = num//10
    return nums



def proper(A):
    for i in range(len(A) - 1):
        if A[i]<A[i+1]:
            return False

    return True


t = int(input())  # read a line with a single integer
for g in range(1, t + 1):
    num = [int(s) for s in input().split(" ")]
    n=num[0]
  
    tidy=[]
    for i in range(0,n+1):
        if(proper(split(i))==True):
            tidy.append(i)

    print("Case #{}: {}".format(g,tidy[-1]))


