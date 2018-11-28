# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = input() # read a list of integers, 1 in this case
    tidyNum = [0 for s in range(1, t + 1)]
    for numbers in range(1, int(n)+1):
        #print("NUmbers: " + str(numbers))
        tN = 0
        maxNum = 0
        isTidy = True
        for num in str(numbers):
##            print("this is num: " + num)
##            print("this is numbers: " + str(numbers))
            if int(num) >= maxNum:
                maxNum = int(num)
            else:
                isTidy = False
                break;
        if isTidy:
            tidyNum[i-1] = numbers

    print("Case #{}: {}".format(i, tidyNum[i-1]))
    # check out .format's specification for more formatting options

