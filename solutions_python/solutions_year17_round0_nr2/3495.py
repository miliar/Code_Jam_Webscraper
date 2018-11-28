

def main(input):
    file = open(input)
    txt = file.read().split()
    file.close()

    file = open("result.txt", 'w')
    i = 0
    while i < int(txt[0]):
        num = int(txt[i+1])
        result = num
        pos = checkAscendentDigits(num)
        while not pos[0]:
            toRest = pow(10,pos[1]-1)
            result = list(str(result))
            if result[pos[1]-1] == 0:
                result[pos[1]-1] = '9'
                result[pos[1]] = str(int(result[pos[1]])-1)
            else:
                result[pos[1]-1] = str(int(result[pos[1]-1]) - 1)

            j = pos[1]
            while j < len(result):
                result[j] = '9'
                j += 1
            result = ''.join(result)
            num = int(result)
            result = num
            pos = checkAscendentDigits(num)
        i += 1
        file.write("Case #"+str(i)+": "+str(result)+"\n")

    file.close()


def checkAscendentDigits(num):
    previousDigit = 9
    pos = 0
    for digit in str(num):
        if digit < previousDigit: return False, pos
        previousDigit = digit
        pos += 1
    return True, -1


def convertToBase3(num):

    newNum = 0
    i = 0
    while num/3 >= 0:
        newNum = newNum + (num%3)*(pow(10,i))
        num /= 3
        i += 1
        if num == 0: return newNum

main("B-large.in")