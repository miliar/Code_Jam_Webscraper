'''
Created on 8 apr. 2017

@author: windows7
'''

def whereToSort(m):
    listM = list(m)
    for i in range(1,len(listM)):
        if (int(listM[i]) < int(listM[i-1])):
            for j in range(1,i):
                if (int(listM[i-(j)]) != int(listM[i-(j+1)])):
                    pos = i-j+1
                    return pos
            return 1
    return 0


def tidyTheNumbers(untidyNums):
    unsortedPos = whereToSort(untidyNums)
    if (unsortedPos == 0):
        return untidyNums
#         print (untidyNums + " is tidy!")
    else:
        untidyList = list(untidyNums)
        toSubtract = int("".join(untidyList[unsortedPos:])) + 1
        untidyInt = int("".join(untidyList))
        tidyInt = untidyInt - toSubtract
#         print (untidyNums + " is not tidy on position " + str(unsortedPos))
        return str(tidyInt)
        print("Untidy: " + untidyNums + " Now tidy: " + str(tidyInt))
    
    
    
if __name__ == "__main__":
    # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    t = int(input())  # read a line with a single integer
        
    for i in range(1, t + 1):
        n = input() # read one line    
        tidyNum = tidyTheNumbers(n)
        print("Case #{}: {}".format(i, tidyNum))
        # check out .format's specification for more formatting options