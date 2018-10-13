from math import sqrt
inputfile = open('C-small-attempt0.in', 'r')
outputfile = open('C-small-attempt0.out', 'w')
count = 0
def ispalindrome(word):
    return word == word[::-1]

n = int(inputfile.readline())
for i in range(0, n):
    numbers = inputfile.readline().split()
    therange = [int(numbers[0]), int(numbers[1])]
    for j in range(therange[0], therange[1] + 1):
        num1 = str(j)
        num2 = sqrt(j)
        if num2 != int(num2):
            num2 = 'rubbish'
        else:
            num2 = str(int(num2))
        if ispalindrome(str(j)) and ispalindrome(num2):
            count += 1
    outputfile.write('Case #' + str(i +1) + ': '+ str(count) + '\n')
    count = 0
    
