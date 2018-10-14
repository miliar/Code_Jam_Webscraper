from math import *

def recicledNums(inputText):
    outPut = open("output","w")
    inputText = open(inputText)
    cases =  int(inputText.readline())
    
    for case in range(cases):
        low, top = map(int, inputText.readline().split(" "))
        numbers = range(low,top+1)
        numsUsed = []
        combinations = 0
        i = 0
        while i < len(numbers):
            num = numbers[i]
            if num not in numsUsed:
                combinations += getPairs(low, top, num, numbers, numsUsed)
            i += 1
        print combinations     
        outPut.write("Case #"+str(case+1)+": "+ str(combinations) +"\n")      


def getPairs(low, top, num, numbers, numsUsed):
    pairs = [num]
    numsUsed.append(num)
    i=1
    while i < len(str(num)):
        tempNum = int(str(num)[-i:] + str(num)[:-i])
        if tempNum <= top and tempNum >= low and (tempNum not in pairs):
            numsUsed.append(tempNum)
            pairs.append(tempNum)
        i += 1

    if len(pairs) > 1:
        combinations = len(pairs)*(len(pairs)-1)/2
        return combinations
    else:
        return 0


if __name__ == "__main__":
    #b = getPairs(10,60000,12345,range(10,60000+1))
    a = recicledNums("C-small-attempt0.in")
