 #! /usr/bin/env python3


def minusOne(word):
    return str(int(word)-1)

def disassemble(N):
    temp = str(N)
    number = []
    for char in temp[::-1]:
        number.append(char)
    return number


def reassemble(list):
    return int(''.join(list[::-1]))

# import test
file = open('/Users/20wanga/Documents/python work/Google jam/test.txt', "r")
setOfNumbers = []
c = 1

for line in file:
    setOfNumbers.append(line.strip())
for number in setOfNumbers:
    N = int(number)
    number = disassemble(N)
    for i in range(0, len(number)-1):
        if number[i] >= number[i+1]:
            continue
        else:
            number[i+1] = minusOne(number[i+1])
            for q in range(0,i+1):
                number[q] = '9'
    with open("/Users/20wanga/Documents/python work/Google jam/output.txt", "a") as myfile:
        myfile.write("Case #" + str(c) + ": " +str(reassemble(number)) + '\n')
    c += 1
