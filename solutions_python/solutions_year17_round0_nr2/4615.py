line_count = int(raw_input())

def isAscending(number):
    number_str = str(number)
    return ''.join(sorted(number_str)) == number_str

def maximumAscendingNumber(number):
    if isAscending(number):
        return number
    else:
        return maximumAscendingNumber(number-1)

for i in range(line_count):
    targetNumber = int(raw_input())
    print 'Case #{}: {}'.format(i+1, maximumAscendingNumber(targetNumber))
