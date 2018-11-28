'''
Created on Apr 14, 2012

@author: arcra
'''

def DancingGooglers(line):
    numbers = line.split()
    S = int(numbers[1])
    P = int(numbers[2])
    
    numbers = numbers[3:]
    
    possibleSurprisingScore = P*3-4
    
    necessaryScore = possibleSurprisingScore+2
    
    possibleCount = 0
    sureCount = 0
    
    
    if P > 1:
        for num in numbers:
            num = int(num)
            if num >= necessaryScore:
                sureCount = sureCount + 1
            elif num == possibleSurprisingScore or num == possibleSurprisingScore+1:
                possibleCount = possibleCount + 1 
    else:
        for num in numbers:
            num = int(num)
            if num >= necessaryScore:
                sureCount = sureCount + 1
    
    if possibleCount > S:
        possibleCount = S
    
    return str(possibleCount + sureCount)

def Wrapper():
    inputFile = open("B-large.in", "r")
    lines = inputFile.readlines()
    inputFile.close()
    
    lines = lines[1:]
    
    caseCount = 1
    outputFile = open("output_DancingGooglers_large.out", "w")
    
    for line in lines:
        result = DancingGooglers(line)
        outputFile.write('Case #' + str(caseCount) + ": " + result + "\n")
        caseCount = caseCount + 1
    
    outputFile.close()

if __name__ == '__main__':
    Wrapper()