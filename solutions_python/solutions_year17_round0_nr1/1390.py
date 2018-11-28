def Ans(pancakes,K):
    pancakes=list(pancakes)
    index=0
    flips=0
    while index<len(pancakes):
        if(pancakes[index]=='-'): #Flip the next K pancakes
            flips+=1
            if(index+K>len(pancakes)): return "IMPOSSIBLE"
            else:
                for cake in range(K):
                    if(pancakes[index+cake]=='-'): pancakes[index+cake]='+'
                    else: pancakes[index+cake]='-'
        index+=1
    return str(flips)


numCases=int(raw_input())
for case in range(numCases):
    line=raw_input().split(" ")
    pancakes=line[0]
    K=int(line[1])
    print("Case #"+str(case+1)+": "+Ans(pancakes,K))
