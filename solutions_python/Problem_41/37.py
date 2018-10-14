import fileinput
def findNextNum(num):
    num = "0" + str(num)
    for i in range(len(num)-1,0,-1):
        prevNum = num[i]
        curNum = num[i-1]
        if curNum < prevNum:
            allNums = [x for x in num[i:]]
            smallestNum = min([x for x in allNums if x > curNum])
            allNums.remove(smallestNum)
            allNums.append(curNum)
            allNums.sort()
            newNum = num[:i-1]+smallestNum+"".join(allNums)
            return int(newNum)
    assert(False)

def main():
    it = fileinput.input()
    count = int(it.next())
    counter = 1
    for l in it:
        print "Case #%d: %d" % (counter,findNextNum(int(l)))
        counter += 1
    assert counter == count+1

if __name__ == "__main__":
    main()
