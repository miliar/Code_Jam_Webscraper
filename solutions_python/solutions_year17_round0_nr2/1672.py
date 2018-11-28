
def result(n):
    
    strN = [c for c in str(n)]
    sortedK = sorted(strN)
    #print(strN,sortedK,sep="#")
    if strN == sortedK:
        return n
    
    nn = jump(n)
    #print("jumped: ",n," # ",nn  )
    return result(nn)
    
def jump(n):
    strN = [p for p in reversed([c for c in str(n)])]
    res = []
    for i in range(len(strN)-1):
        #print(strN,i,strN[i],strN[i+1])
        if strN[i] < strN[i+1]:
            res = ['9']*(i+1)
            res.append(chr(ord(strN[i+1])-1))
            res.extend(strN[i+2:])
            return int("".join(reversed(res)))
        else:
            res.append(strN[i])


t = int(input()) 
for i in range(1, t + 1):
    n = [int(s) for s in input().split(" ")][0]
    print("Case #{}: {}".format(i, result(n)))
