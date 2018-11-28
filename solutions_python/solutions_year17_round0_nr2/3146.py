def tidy_fix(n):
    x = list(str(n))
    for i in range(0, len(x) - 1):
        if x[i] > x[i + 1]:
            return int(''.join(x[:i] + [str(int(x[i]) - 1)] + ['9'] * len(x[i + 1:])))
    return n


def previous_tidy(y):
    x = 0
    while x != y:
        x = y
        y = tidy_fix(x)
    return y


fr = open('B-large.in', 'r')
fw = open('tidy-large-output.txt', 'w+')
numcases = int(fr.readline())
idline = 0

for x in range(1, numcases + 1):
    idline += 1
    inputs = fr.readline().replace('\n', '').split(' ')
    finputs = [int(inputr) for inputr in inputs]
    foutputs = [previous_tidy(i) for i in finputs]
    for line in foutputs:
        fw.write("Case #" + str(idline) + ": " + str(line) + '\n')
