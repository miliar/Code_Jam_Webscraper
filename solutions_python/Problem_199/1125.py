import string

def sol(pancakes, width):
    pancakes = [c for c in pancakes]
    i = 0
    count = 0
    while i < len(pancakes):
        if pancakes[i] == '-':
            count += 1
            if i+width > len(pancakes):
                return "IMPOSSIBLE"
            for j in range(i,i+width):
                if pancakes[j] == '-':
                    pancakes[j] = '+'
                else:
                    pancakes[j] = '-'
        i += 1

    return count



fIn = open('input.in', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    print(case)
    if case > 0:
        k = line.split()[0]
        l = int(line.split()[1])
        fOut.write("Case #"+str(case)+": "+str(sol(k,l))+"\n")
    case += 1