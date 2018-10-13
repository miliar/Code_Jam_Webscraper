import sys

def main(argv=sys.argv):
    filename = argv[1]
    case = 0
    with open(filename+".in", 'r') as inputFile, open(filename+".out",'w') as outputFile:
        N = inputFile.readline()
        for line in inputFile.readlines():
            case += 1
            #print(line)
            line=line.split()
            max=line[0]
            shyness=map(int, list(line[1]))
            
            result = countNecessaryFriends(shyness)
            caseResult="Case #{}: {}".format(case,result)
            outputFile.write(caseResult+'\n')
            print(caseResult)


def countNecessaryFriends(shyness):
    length = len(shyness)
    index = 0
    curIndex = 0
    result = 0
    while (index < length):
        
        while(curIndex <= index and curIndex < length):
            index += shyness[curIndex]
            curIndex += 1

        if index >= length:
            break;

        if shyness[index] == 0:
            end = index
            while(end < length and shyness[end]==0):
                end+=1
            result += end-index
            index = end

        #print("{}\ncurIndex:{} index:{}".format(shyness,curIndex,index))

    return result

if __name__=="__main__":
    main()
