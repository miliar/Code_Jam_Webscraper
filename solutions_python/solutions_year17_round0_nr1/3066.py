def min_flops(pancakes, K):

    pancakesS=[]
    for s in range(len(pancakes)):
        pancakesS.append(pancakes[s])

    count = 0
    for i in range(len(pancakesS)-K+1):
        if pancakesS[i]=="-":
            count +=1
            for j in range(K):
                if pancakesS[i+j]=="-":
                    pancakesS[i+j]="+"
                else:
                    pancakesS[i+j]="-"

    for i in range(len(pancakesS)): # could check only last ones
        if pancakesS[i]=="-":
            return("IMPOSSIBLE")

    return(count)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    pancakes, k = input().split(" ")
    K=int(k)
    print("Case #{}: {}".format(i, min_flops(pancakes,K)))
     # check out .format's specification for more formatting options
