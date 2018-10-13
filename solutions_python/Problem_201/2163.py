import re
import math

input = open('input.in')
output = open('output.out' ,'w')

amount = int(input.readline())
counter = 1
while counter <= amount:
    line = re.match(r'(\d+) (\d+)',input.readline())
    N = int(line.group(1))
    S = int(line.group(2))
    row = '0' * N 
    while S:
        all = re.findall(r'0+',row)
        length = sorted(len(i) for i in all)
        longest = length[-1]
        if S == 1:
            break
        new = '0' * (math.ceil(longest / 2) - 1) + '1' + '0' * math.floor(longest / 2)
        row = re.sub(r'0{%s}' % longest,new,row,1)
        S = S - 1
    output.write('Case #' + str(counter) + ': ' + str(math.floor(longest / 2)) + ' ')
    if longest == 0:
       output.write('0\n')
    else:
        output.write(str(math.floor((longest - 1) / 2)) + '\n')
    counter = counter + 1

input.close()
output.close()