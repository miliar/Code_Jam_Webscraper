def tidy(num):
    numStr = str(num)
    numL = [char for char in numStr]
    sortedNums = sorted(numL)
    # if(numL == sortedNums):
    #     print(numL)
    #     print(sortedNums)
    return (numL == sortedNums)

def main():

    #read input
    fileOpen = open("files.txt",'r')
    inputNum = fileOpen.readline()
    inputNum = 1000
    lineNum = 1
    writeFile = open("output.txt", 'w')
    for line in fileOpen:
        lastTidy = 0

        for num in range(int(line)+1):
            if num >= lastTidy and tidy(num):
                lastTidy =  num


        writeFile.write("Case #" + str(lineNum) +  ": " + str(lastTidy) + "\n")

        lineNum+=1

main()
