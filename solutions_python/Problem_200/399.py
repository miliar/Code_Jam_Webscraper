
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # #get pancake and k size

    maxNum = int(raw_input())

    tidy = 1
    #count backwards from maxNum
    #check current number
    currNum = maxNum
    while currNum > 0:
        #print currNum
        tidy = 1
        currNumStr = str(currNum) #convert to str
        length = len(currNumStr)

        #check if its a tidy num
        currNumStr = list(currNumStr) #convert to list
        currLargestDigit = int(currNumStr[length - 1])
        powerOfTen = 0
        nines = 0
        countNines = 1

        for index in range(length - 1, -1, -1):
            currDigit = int(currNumStr[index])
            if currDigit == 9 and countNines == 1: #only count continues 9's
                nines += 1
            else:
                countNines = 0
            if currDigit <= currLargestDigit:
                currLargestDigit = currDigit
                powerOfTen += 1
            else:
                #not tidy
                tidy = 0
                break

        if tidy == 1:
            print("Case #{}: {}".format(i, currNum))
            break
        else:
            #decrement currNum
            #currNum -= 10**(powerOfTen-1)
            #print "nines: ", nines
            currNum -= 10**(nines)
