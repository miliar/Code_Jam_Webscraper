def checkTidy (num):
    return list(num) == sorted(num)

def smallestTidyNumber(num):
    numpos = 0
    while checkTidy(num) == False:
        num = "0" + num
        for j in range (0,len(num)-1):
            if int(num[j]) <= int(num[j+1]):
                numpos = j+1
            else :
                break
        num = num[:numpos] + str((int(num[numpos])-1)%10) + "9"*(len(num)-numpos-1)
    return str(int(num))


testCases = int(input())
for i in range(testCases):
    num = input()
    print("Case #" + str(i+1) + ": " + smallestTidyNumber(num))
