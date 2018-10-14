#!/usr/bin/python2.6 -tt

from math import sqrt

def openFile(path, right):
    file = open(path, right)
    return file
    
def closeFile(file):
    file.close()

def parseFile(file):
    firstLine = next(file)
    case = 1
    i = 0
    matrice = {}
    while case <= int(firstLine[:-1]):
        matrice[case] = next(file).split()
        case += 1
    return matrice
    
def getReverse(number):
    x = int(number)
    return int("".join(list(reversed(str(x)))))    

def is_square(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1
        if ans*ans != x: 
            return None
        else:
            return True
    else:
        return None

def isSquare(num):    
    isSqr = False
    
    if is_square(int(num)):
        if isFair(sqrt(int(num))):
            isSqr = True
    
    return isSqr
    
def isFair(number):
    isFair = False
    
    if int(number) == getReverse(int(number)):
        isFair = True
            
    return isFair
    
def howManyFas(tab):
    compteur = 0
    for i in range(int(tab[0]), int(tab[1])+1):
        if isFair(int(i)) and isSquare(int(i)):
            compteur += 1
            
    return compteur

def main():
    path = "C-small-attempt0.in"
    output = "C-small"
    file = openFile(path, "rU")
    outputFile = openFile(output, "wb")
    
    cases = parseFile(file)
    i = 1
    for case in cases.values():
        outputFile.write("Case #" + str(i) + ": " + str(howManyFas(case))+"\n") 
        i += 1
    
    closeFile(file)
    closeFile(outputFile)
	
#launch the main function
if __name__ == '__main__':
	main()