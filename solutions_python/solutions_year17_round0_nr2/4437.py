

def isNumTidy(num):
    """Checks whether the given number is tidy"""
    numChars = str(num)
    #print numChars, len(numChars)
    for i in xrange(1, len(numChars)):
        if int(numChars[i]) < int(numChars[i-1]):
            #print numChars[i], numChars[i-1]
            return False
    return True

def last_tidy_number(n):
    """Gets the greatest tidy number less than n."""
    if n < 9 :
        return n
    for i in xrange(n,8,-1):
        if isNumTidy(i):
            return i

def efficient_last_tidy_num(num):
    """Efficient way to get the last tidy number."""
    numChars = str(num)
    if len(numChars) == 1:
        return num
    lastTidyNum = numChars[0]

    for i in xrange(1, len(numChars)):
        if int(numChars[i]) >= int(numChars[i-1]):
            lastTidyNum += numChars[i]
        else:
            index = lastTidyNum.index(numChars[i-1])
            lastTidyNum = lastTidyNum[:index]
            lastTidyNum += str(int(numChars[i-1]) - 1)
            lastTidyNum += "9"*(len(numChars) - 1 - index)
            break
    return int(lastTidyNum)

#Testing code
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #seq = raw_input()
    num = int(raw_input())
    print "Case #{}: {}".format(i, efficient_last_tidy_num(num))
  # check out .format's specification for more formatting options
