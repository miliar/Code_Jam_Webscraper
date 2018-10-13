def getFlips(pancakes, K):
    flips=0
    for i in range(len(pancakes)):
        if pancakes[i]=="-":
            if K + i <= len(pancakes):
                for j in range(i, i + K):
                    if pancakes[j]=="-":
                        pancakes[j]="+"
                    else:
                        pancakes[j]="-"
                flips+=1
            else:
                return "IMPOSSIBLE"
    return flips
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    pancakes, K = input().split(" ")
    K=int(K)
    pancakes=list(pancakes)
    print("Case #{}: {}".format(i, getFlips(pancakes, K)))