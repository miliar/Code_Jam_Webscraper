
def validateTidyNumber(tidyNum):
    strTidyNum = str(tidyNum)
    for i,x in enumerate(strTidyNum):
        try:
            if strTidyNum[i+1] < x:
                return False
        except Exception as e:
            pass
    return True

def findLastTidyNumber(tidyNum):
    currentNum = int(tidyNum)
    while(not validateTidyNumber(currentNum)):
        #print(currentNum)
        currentNum = currentNum - 1
    return currentNum


def tidyNumbers(tidyNum):
    return findLastTidyNumber(tidyNum)


t = int(input())
for i in range(1, t+1):
    num = input()
    print("Case #{}: {}".format(i,tidyNumbers(num)))
