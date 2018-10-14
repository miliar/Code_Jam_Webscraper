



def isTidy(testVal):
    last = str(testVal)[0];
    for ch in str(testVal)[1:]:
        if ch < last: return False
        last = ch
    return True

def lastTidy(num):
    if isTidy(num): return num
    num = str(num)
    maxCh = max(num)
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            for j in range(i - 1, -1, -1):
                if num[j] != num[i]:
                    return int(num[:j+2] + "0"*(len(num) - (j + 2))) - 1
            return int(num[0] + "0"*(len(num) - 1)) - 1


if __name__ == '__main__':
    inputName = "largeTidy.txt"
    outputName = "outputLargeTidy.txt"
    f = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/" + inputName,'r')
    w = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/" + outputName,'w')
    case = 0
    for line in f:
        if case != 0:
            w.write("Case #" + str(case) + ": " + str(lastTidy(int(line.strip()))) + "\n")
        case += 1
    f.close()
    w.close()



    # print(lastTidy(124444111244679))


    # # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
    # # This is all you need for most Google Code Jam problems.
    # t = int(input())  # read a line with a single integer
    # for i in range(1, t + 1):
    #     sol = lastTidy(i)
    #     print("Case #{}: {}".format(i, sol)
    #     # check out .format's specification for more formatting options
