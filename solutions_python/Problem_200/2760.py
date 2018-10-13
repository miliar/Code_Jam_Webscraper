

with open('small.in', 'r') as f:
    lines = f.readlines()
def isSorted(array):
    sorted = True
    for i in xrange(0,len(array)-1):
        if array[i] > array[i+1]:
            change(array,i)
            sorted = False
            return sorted
    return sorted
def convertToList(num):
    numbers = []
    for i in num:
        numbers.append(long(i))
    return numbers
def convertToNumber(numList):
    s = map(str, numList)
    s = ''.join(s)
    s = int(s)

    return s

row = 0
for line in lines[1:]:
    numbers = []
    row += 1
    num = long(line)
    sorted = False
    def change(array, i):
        numbers[i] = numbers[i] - 1
        for k in xrange(i+1, len(array)):
            numbers[k] = 9

    while (sorted == False):
        otherNumber = str(num)
        numbers = convertToList(otherNumber)
        if isSorted(numbers):
            print 'Case #%r: %r' %(row, int(otherNumber))
            sorted = True
        num = convertToNumber(numbers)
