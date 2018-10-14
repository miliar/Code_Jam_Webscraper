import re

input = open('input.in')
output = open('output.out','w')

amount = int(input.readline())
counter = 1
while counter <= amount:
    line = re.match(r'(\d*)',input.readline())
    num = line.group(1)    
    i = 0
    while i < len(num) - 1:
        if num[i] <= num[i + 1]:
            i = i + 1
            continue
        if num[i] > num[i + 1]:
            num = num[:i] + str(int(num[i]) - 1) + '9' * (len(num) - i - 1)
            if i > 0:
                i = i - 1
            continue
    intger = re.match(r'0*(\d*)',num)
    num = intger.group(1)
    output.write('Case #' + str(counter) + ': ' + num + '\n')
    counter = counter + 1
output.close()
