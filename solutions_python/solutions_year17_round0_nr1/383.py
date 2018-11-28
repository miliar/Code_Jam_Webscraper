
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    # #get pancake and k size

    str = raw_input()
    #print "input is", str
    #k size is the last char so...
    #print k
    #remove space and int from end of str
    for index in range(0, len(str)): #OMG double+ digit nums....
        if str[index].isspace():
            k = int(str[index:])
            #print k
            str = str[:index]
            break
    #print "removed", str
    #length
    length = len(str)
    #last char indx
    lastCharIdx = length - 1
    stopIdx = lastCharIdx - (k - 1)
    #print "stopidx", stopIdx
    str = list(str) #great, have to turn string into a list first
    count = 0
    success = 1
    #print str
    for index in range(0, stopIdx + 1): #wtf, it excludes last num
        #if not +
        #print "current pancake: ", str[index], " ", index
        if str[index] == '-':
            count += 1
            #flip pancakes
            for subindex in range(0, k): #great, it excludes k
                currIndex = index + subindex
                if str[currIndex] == '+':
                    str[currIndex] = '-'
                else:
                    str[currIndex] = '+'
        #print "flipping"
        #print str
    #check if rest of pancakes are okay
    for index in range(stopIdx, lastCharIdx + 1):
        if str[index] == "-":
            success = 0
            break
    if success == 1:
        #str = "".join(str) #join it back together, hopefully
        #print str
        print("Case #{}: {}".format(i, count))
    else:
        print("Case #{}: IMPOSSIBLE".format(i))
        #print "Impossible"
    #print "num removed", str
        #print("Case #{}: {} {}".format(i, n + m, n * m))
        # check out .format's specification for more formatting options

