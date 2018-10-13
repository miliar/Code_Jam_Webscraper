t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s, k = [e for e in input().split(" ")]  # read a list of integers, 2 in this case
    k=int(k)
    s=list(s)
    count=0
    for j in range(0,len(s)):
        if (s[j]=="-"):
            if(len(s)-j<k): 
                count="IMPOSSIBLE"
                break
            count+=1
            for l in range(j,j+k):
                if (s[l]=="-"):
                    s[l]="+"
                else :
                    s[l]="-"
    print("Case #{}: {}".format(i, count))