# -*- coding: UTF-8 -*-
#!/usr/bin/env python

inputName  = 'C-large.in'
outputName = 'output.txt'

def decToBin(decCandy):
    binCandy = []
    while decCandy > 0:
        y = decCandy % 2
        binCandy.append(y)
        decCandy = int(decCandy / 2)
    if len(binCandy) < 20:
        for i in range(20-len(binCandy)):
            binCandy.append(0) 
    return binCandy

def printList(listCandy):
    for item in listCandy:
        print(item)

def xorList(listCandy):
    x = listCandy[0]
    for i in range(1, len(listCandy)):
        x = listCandy[i] ^ x
    return x

def splitCandy(decListCandy):
    minCandy = 1000000
    summ = 0
    for item in decListCandy:
        if item < minCandy:
            minCandy = item
        summ += item
    return summ - minCandy
        

def main():
    print("Google Code Jam:\nCandy Splitting")
    inputFile  = open(inputName, 'r')
    outputFile = open(outputName, 'w')
    nmrCases = int(inputFile.readline().rstrip()) #количество вариантов
    print("nmrCases =", nmrCases)
    for case in range(nmrCases):
        binListCandy = []
        nmrCandy = int(inputFile.readline().rstrip())
        decListCandy = inputFile.readline().rstrip().split()
        for i in range(len(decListCandy)):
            decListCandy[i] = int(decListCandy[i])
        print(nmrCandy, decListCandy)
        for candy in decListCandy:
            binListCandy.append(decToBin(candy))
        
        xorListCandy = xorList(decListCandy)
        if xorListCandy == 0:
            summ = splitCandy(decListCandy)
        else:
            summ = 'NO'
        printList(binListCandy)
        print("xor =", xorListCandy)
        outputFile.write("Case #" + str(case+1) + ": " + str(summ) + "\n")
    inputFile.close()
    outputFile.close()
    print("Done")

if __name__ == '__main__':
    main()