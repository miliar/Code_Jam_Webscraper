def main():
    file = open(raw_input("Select a file for processing: "))
    numcases = int(file.readline())
    index = 1
    for line in file:
        words = line.split(" ")
        numswitchers = int(words[0])
        switchers = []
        for i in range(1, numswitchers + 1):
            switchers.append(words[i])
        numkillers = int(words[numswitchers + 1])
        killers = []
        for i in range(numswitchers + 2, numswitchers + numkillers + 2):
            killers.append(words[i])
        invoked = words[-1].strip()
        elementlist = []
        for char in invoked:
            elementlist.append(char)
            if len(elementlist) > 1:
                for switcher in switchers:
                    el1 = switcher[0]
                    el2 = switcher[1]
                    res = switcher[2]
                    if elementlist[-1] == el1 and elementlist[-2] == el2 or elementlist[-1] == el2 and elementlist[-2] == el1:
                        del elementlist[-1]
                        del elementlist[-1]
                        elementlist.append(res)
                for killer in killers:
                    el1 = killer[0]
                    el2 = killer[1]
                    if el1 in elementlist and el2 in elementlist:
                        elementlist = []
        string = ""
        for element in elementlist:
            string = string + element
            string = string + ", "
        
        print "Case #" + str(index) + ": [" + string[0:-2] + "]"
        index = index + 1

if __name__ == '__main__':
    main()
