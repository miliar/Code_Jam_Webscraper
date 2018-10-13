"""2k17 CodeJam Second Question."""

# 4923765
# Right most digit (5) scan left to find first digit greater (6, pos 5) and decrease it by one
# Turn everything to the right of decreased into 9
# 4923759
# Starting from decreased (pos 5), repeat
# 4923699
# 4899999


def TidyNumbers(number):
    """Find largest number in range(1, number) that has digits sorted in ascending order."""
    numberList = [int(x) for x in reversed(str(number))]
    while list(reversed(numberList)) != sorted(list(reversed(numberList))):
        for i in range(len(numberList)):
            if numberList[i] != 9:
                temp = [x for x in numberList[i:] if x > numberList[i]]
                if not temp:
                    continue
                index = numberList.index(temp[0])
                numberList[index] -= 1
                numberList[:index] = [9] * len(numberList[:index])
                break
    return str(int(''.join(map(str, list(reversed(numberList))))))


inputfile = open('inputTidyNumbersLarge.txt', 'r')
outputfile = open('outputTidyNumbersLarge.txt', 'w')

n = int(inputfile.readline())

for i in range(n):
    number = int(inputfile.readline().rstrip())
    outputfile.write("Case #" +
                     str(i + 1) +
                     ": " +
                     str(TidyNumbers(number)) +
                     "\n")
