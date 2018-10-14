import fileinput
import math

def read_file(File):
    text = File.read()
    lines = text.split('\n')
    return lines

def read_fileInt(File):
    text = File.read()
    lines = text.split('\n')
    for line in range(len(lines)):
        lines[line] = int(lines[line])
    return lines

def ispalindrome(word):
    return word == word[::-1]

def checkPalindrome(a):
    palindrome = True
    stringVersion = str(a)
    length = len(stringVersion)
    for p in range(length):
        if (stringVersion[p] != stringVersion[length-1-p]):
            palindrome = False
            break
    return palindrome

def getNextFairSquare(n):
    found = False
    x = int(math.sqrt(n))
    while (found == False):
        x += 1
        if ispalindrome(str(x)) and ispalindrome(str(x*x)):
            return x*x

def addFairNums(minN, maxN):
    x = minN
    fairNumFile = open('fairsquarenumbers.txt','r+')

    while (x < maxN):
        x = getNextFairSquare(minN)
        fairNumFile.write('\n' + str(x))
    fairNumFile.close()

def getAllFairSquare(n, file):
    x = 1
    nums = [1]
    while (x < n):
        x = getNextFairSquare(x)
        nums.append(x)
        file.write('\n' + str(x))
    return nums

inputFile = open('input.txt','r')
lines = read_file(inputFile)
inputFile.close()

fairNumFile = open('fairsquarenumbers.txt','r+')

n = int(lines[0]) #number of test cases

maxB = 0

for j in range(n):
    parts = lines[j + 1].split(" ")
    B = parts[1]
    maxB = max(int(B),maxB)
    
if maxB > 10**14:
    fairNumFile.truncate()
    genNums = getAllFairSquare(10**14,fairNumFile)
else:
    genNums = read_fileInt(fairNumFile)
    
fairNumFile.close()
    
for i in range(n):
    parts = lines[i + 1].split(" ")
    A = parts[0]
    B = parts[1]
    number = 0
    numbers = []

    ran = range(int(A), int(B) + 1)
    for b in genNums:
        if b in ran:
            number += 1
            
    print("Case #" + str(i+1) + ": " + str(number))
