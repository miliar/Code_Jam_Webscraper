#### Problem B. Lawnmower ####

from itertools import product

# input
filename = "B-small-attempt0.in"
lines = (line.rstrip('\n') for line in open(filename))
T = int(lines.__next__())

# output
output = open('output', 'w+')

# test case loop
for caseIdx in range(T):
    [n, m] = map(int, lines.__next__().split(' '))
    lawn = [lines.__next__().split(' ') for _ in range(n)]
    #print(lawn)

    # doable?
    doable = True
    for (i, j) in product(range(n), range(m)):
        # Zeile?
        if all(map(lambda x: x <= lawn[i][j], lawn[i])):
            continue

        # Spalte?
        if all(map(lambda x: x <= lawn[i][j], [lawn[k][j] for k in range(n)])):
            continue

        # neither
        doable = False
        break

    msg = 'YES' if doable else 'NO'
    output.write('Case #' + str(caseIdx + 1) + ': ' + msg + '\n')


output.close()
print(open('output', 'r').read())
