pancakeoutput = 'A-large.out'
pancakeinput = 'A-large.in'

with open(pancakeoutput, 'w') as f:
    inputlines = [] 
    with open(pancakeinput, 'r') as g:
        inputlines = g.readlines()
    numcases = int(inputlines.pop(0))
    for x in range(numcases):
        case = inputlines.pop(0)
        case_sep = case.split()
        pancakes = case_sep[0]
        k = int(case_sep[1])

        num_flips = 0
        i = 0
        while ((pancakes.count('+') != len(pancakes)) and (i <= len(pancakes)-k)):
            if pancakes[i] != '+':
                for j in range(k):
                    temp = list(pancakes)
                    if pancakes[i+j] == '+':
                        temp[i+j] = '-'
                        pancakes = ''.join(temp)
                    else:
                        temp[i+j] = '+'
                        pancakes = ''.join(temp) 
                num_flips += 1
            i += 1

        flips = str(num_flips)
        if (pancakes.count('+') != len(pancakes)):
            flips = "IMPOSSIBLE"

        strtowrite = 'Case #'+str(x+1)+": "+flips+"\n"
        f.write(strtowrite)

