import math

FILE = open("C-large.in","r")
OUTPUT = open("C-large.out","w")

cases = FILE.readline()

for i in range(0,int(cases)):
    temp = FILE.readline().rstrip('\n').split(" ")
    n = int(temp[0])
    temp = FILE.readline().rstrip('\n').split(" ")
    sum = 0
    least = 0
    xored = 0
    for j in range(0,n):
        xored = xored ^ int(temp[j])
        sum += int(temp[j])
        if least == 0 or (int(temp[j]) < least):
            least = int(temp[j])
    if xored == 0:
        OUTPUT.write('Case #' + str(i + 1) + ': ' + str(sum-least) + '\n')
    else:
        OUTPUT.write('Case #' + str(i + 1) + ': NO \n')
        
FILE.close()
OUTPUT.close()

