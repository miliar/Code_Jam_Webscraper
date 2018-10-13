import re

input = open('input.in')
output = open('output.out','w')

amount = int(input.readline())
counter = 1
while counter <= amount:
    line = input.readline()
    x = re.match(r'([+-]*) (\d*)',line)
    row = x.group(1)
    k = int(x.group(2))
    i = 1
    time = 0
    while i <= len(row) - k + 1:
        if row[i - 1] == '-':
            turn = re.sub(r'[-]','0',row[i - 1:i + k - 1])
            turn = re.sub(r'[+]','-',turn)
            turn = re.sub(r'[0]','+',turn)
            row = row[:i - 1] + turn + row[i + k - 1:]
            time = time + 1
        i = i + 1
    if re.match(r'.*[-].*',row):
        output.write('Case #' + str(counter) + ': ' + 'IMPOSSIBLE ' + '\n')
    else:
        output.write('Case #' + str(counter) + ': ' + str(time) + '\n')
    counter = counter + 1
output.close()