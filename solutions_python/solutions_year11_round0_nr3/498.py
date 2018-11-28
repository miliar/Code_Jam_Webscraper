inFile = open("..\input.txt", "r")
outFile = open("..\output.txt", "w")

#def solve(candy):
#    ret = ssub(candy, [], [])
#    if ret == 0 :return "NO"
#    return ret
#    
#def ssub(candy, p1, p2):
#    if len(candy) == 0 :
#        if len(p1) == 0 or len(p2) == 0: return 0
#        if sum(p1) < sum(p2): return 0
#        if sumXOR(p1) == sumXOR(p2):
#            return sum(p1)
#        else: return 0
#    else:
#        c = candy.pop()
#        ret = max(ssub(candy, p1 + [c], p2), ssub(candy, p1 , p2 + [c]))
#        candy.append(c)
#        return ret
#    
def solve2(candy):
    if sumXOR(candy) != 0: return "NO"
    else: return sum(candy) - min(candy)
        
def sumXOR(p):
    ret = 0;
    for c in p:
        ret = ret ^ c
    return ret;

N = int(inFile.readline())
for cnt in range(1, N + 1):
    nc = int(inFile.readline())
    candy = inFile.readline().split()
    for i in range(nc):
        candy[i] = int(candy[i])

    resStr = "Case #" + str(cnt) + ": " + str(solve2(candy)) + "\n"
    
    #if solve2(candy) != solve(candy) :print (resStr)
    #print (sumXOR(candy))
    print (resStr)
    outFile.write(resStr)

inFile.close()
outFile.close()
