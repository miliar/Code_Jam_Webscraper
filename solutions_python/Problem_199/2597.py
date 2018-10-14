import math
t = int(input())
for i in range(1,t+1):
    (pancakes, k) = input().split(" ")
    length = len(pancakes)
    result = 0
    pancakes = list(pancakes)
    for c in range(0,length):
        if (pancakes[c]=='-'):
            result+=1
            for j in range(c, c+ int(k)):
                if(j>=length):
                    result=-1
                    break
                if(pancakes[j]=='-'):
                    pancakes[j]='+'
                else:
                    pancakes[j]='-'
            if(result==-1): break
        if(result==-1): break
    if(result==-1):
        print("Case #{}: IMPOSSIBLE".format(i))
    else:
        print("Case #{}: {}".format(i, result))