import re
with open("A-large.in", "r") as input_lines:
    array = []
    for line in input_lines:
        array.append(line)
a = int(array[0])
if(a>0):
    for caseNumber in range(1,a+1):
        string, panCakes = re.split(' ', array[caseNumber])
        string = list(string)
        panCakes = int(panCakes)
        flip = 0
        impossible = 0
        for index,value in enumerate(string):
            if(value != '+'):
                if len(string)-index >= panCakes:
                    for number in range(0,panCakes):
                        if string[index + number] == '+':
                            string[index + number] = '-'
                        else:
                            string[index + number] = '+'
                    flip = flip+1
                else:
                    impossible = 1
        if(impossible == 0):
            result = "Case #%d: %d" % (caseNumber, flip)
        else:
            result = "Case #%d: IMPOSSIBLE" % (caseNumber)
        with open('output.txt', 'a') as out:
            out.write(result + '\n')
