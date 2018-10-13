def flip (string, K, index):
    if index + K > len(string):
        return string
    else:
        ret = ''
        lst = []
        for i in range(len(string)):
            lst.append(string[i])
        for i in range (index, index + K):
            if lst[i] == '-':
                lst[i] = '+'
            elif lst[i] == '+':
                lst[i] = '-'
        for i in range(0,len(lst)):
            ret=ret+lst[i]
        return ret

with open ('A-large.in.txt') as ifile:
    lines = ifile.readlines()

T = int(lines[0])
res = open('out.txt', 'w')
for cases in range(1, T + 1):
    inp = [str(x) for x in lines[cases].split()]
    K = int(inp[1])
    pancakes = inp[0]
    count = 0

    for i in range (len(pancakes)):
        if pancakes[i] == '-':
            pancakes = flip(pancakes, K, i)
            count+=1

    printer = 'Case #' + str(cases)+ ': '

    if '-' in pancakes:
        res.write (printer + 'IMPOSSIBLE\n')
    else:
        res.write (printer + str(count) + '\n')
