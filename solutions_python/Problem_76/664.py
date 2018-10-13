import itertools
def main():
    output = ""
    f = open("input.txt",'r')
    lines = f.readlines()
    f.close()
    ct = int(lines[0])
    i = 0
    cNum = 1
    while i<ct:
        i+=1
        nums = map(lambda x: int(x),lines[2*i].rstrip("\n").split(" "))
        res = evalNums(nums)
        output += "Case #%d: %s\n"%(cNum, res)
        cNum+=1
    output = output[:len(output)-1]
    print output
    f = open("output.txt",'w')
    f.write(output)
    f.close()

def evalNums(nums):
    bestNum = -1
    bestTup = ()
    cLen = 1
    while cLen<=len(nums):
        inBox = itertools.combinations(nums,cLen)
        for s in inBox:
            lTot = digSum(s)
            rTot = remDSum(nums, s)
            if lTot==rTot:
                trueSum = remSum(nums,s)
                if trueSum>bestNum:
                    bestNum = trueSum
                    bestTup = s
        cLen += 1
    if bestNum>0:
        return bestNum
    else:
        return "NO"
def digSum(tup):
    out = 0
    for x in tup:
        out = out ^ x
    return out
def remSum(nums, inBox):
    return sum(getRem(nums,inBox))
def remDSum(nums, inBox):
    return digSum(getRem(nums,inBox))
def getRem(nums, remove):
    newNums = list(nums)
    for x in remove:
        newNums.remove(x)
    return newNums
if __name__=="__main__":
    main()
#ABFE
