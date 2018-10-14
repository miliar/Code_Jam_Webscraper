def isTiny(strnum):
    for i in xrange(0,len(strnum)-1):
        if strnum[i] > strnum[i+1]:
            return False
    return True

def concatArr(arr):
    result = ""
    for ele in arr:
        result += ele
    return result

globalAnswer = ""

def fixTiny(num):
    global globalAnswer
    globalAnswer = "default"
    fixTinyRec(list(str(num)), 0)
    #print int(globalAnswer.join(""))
    return globalAnswer

def fixTinyRec(strnum, i):
    #print "i : " +  str(i)
    global globalAnswer
    if i == len(strnum)-1:
        if isTiny(strnum):
            globalAnswer = int(concatArr(strnum))
    else:
        if strnum[i] > strnum[i+1]:
            a = int(strnum[i]) - 1
            strnum[i] = str(a)
            for j in range(i+1, len(strnum)):
                strnum[j] = "9"
        fixTinyRec(strnum, i+1)
        while strnum[i] > strnum[i+1]:
            a = int(strnum[i]) - 1
            strnum[i] = str(a)
            for j in range(i+1, len(strnum)):
                strnum[j] = "9"
            fixTinyRec(strnum, i+1)

f = open("B-large(3).in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline().strip()
    print "Case #" + str(x+1) + ": " + str(fixTiny(int(readline)))


'''
print fixTiny(132)
print fixTiny(1000)
print fixTiny(7)
print fixTiny(219)
print fixTiny(10)
print fixTiny(11101111111)
print fixTiny(1234440)
'''