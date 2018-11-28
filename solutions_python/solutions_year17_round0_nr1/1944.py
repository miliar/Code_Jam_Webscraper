'''
Created on 8 avr. 2017

@author: Regis DUPUIS
'''

def permut(pancake):
    if(pancake == "+"):
        return "-"
    else:
        return "+"

def numPermutations(pancakeRowStr, flipperSize):
    nbPerm = 0
    pancakeRowList = list(pancakeRowStr)
    
    while(pancakeRowList.__contains__("-")):
        firstMinusIndex = pancakeRowList.index("-")
        if firstMinusIndex > (len(pancakeRowStr) - flipperSize):
            nbPerm = "IMPOSSIBLE"
            break
        else:
            for indexToPermut in range(firstMinusIndex, flipperSize + firstMinusIndex):
                pancakeRowList[indexToPermut] = permut(pancakeRowList[indexToPermut])
            
            nbPerm += 1
        
    return nbPerm


if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        s, k = input().split(" ")
        
        nbPerm = numPermutations(s, int(k))
        
        print("Case #{}: {}".format(i, nbPerm))
        # check out .format's specification for more formatting options