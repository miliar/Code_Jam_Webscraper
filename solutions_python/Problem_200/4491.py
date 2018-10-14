# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
def tidy(N):
    strN = str(N)
    last = 0
    fail_pos = -1;
    for i in range(0,len(strN)):
        if(int(strN[i]) < last):
            fail_pos = i
            break
        last = int(strN[i])
    if(fail_pos > -1):
        strlen = len(strN) - 1
        for i in range(strlen, fail_pos, -1):
            strN = '%s%s%s'%(strN[:i], '9', strN[i+1:])
            
        for i in range(fail_pos, -1, -1):
            if(int(strN[i]) > 1 and i != 0):
                strN = '%s%s%s'%(strN[:i], str(int(strN[i])-1), strN[i+1:])

            if((i != 0 and (int(strN[i]) < int(strN[i-1])) or int(strN[i]) == 0) ):
                strN = '%s%s%s'%(strN[:i], '9', strN[i+1:])
            elif(i == 0):
                strN = '%s%s%s'%(strN[:i], str(int(strN[i])-1), strN[i+1:])
            else:
                break

    return int(strN)


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N = int(raw_input())
    result = tidy(N)
    print('Case #' + str(i) + ': ' + str(result))

    # check out .format's specification for more formatting options


