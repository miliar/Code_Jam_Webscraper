__author__ = 'abu-abdurahman'
contents = [list.strip() for list in open('B-large.in') ]
numberOfInput = int(contents[0])

def getSolution(co, fa, xz):
    increment = 2
    seconds = 0
    if(xz / increment < co / increment):
        return '%.7f' % (xz/increment)
    while(True):
        without = xz / increment
        withBuying = co/ increment + (xz /(increment + fa))
        if(withBuying < without):
            seconds += (co/increment)
            increment += fa
        else:
            seconds += (xz/increment)
            return '%.7f' % seconds




j = 1
solution = []
for i in range(numberOfInput):
    C, F, X = (contents[j].split())
    j += 1
    solution.append(getSolution(float(C), float(F), float(X)))


output = open('output.txt', 'w')
#output.write('Output \n')
for i in range(1, len(solution) + 1):
    output.write(str('Case #') + str(i) + ': ' + str(solution[i-1]) + '\n' )