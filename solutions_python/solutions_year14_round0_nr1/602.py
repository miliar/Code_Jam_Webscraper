title = 'A'
scale = 'small'

fpout = open(title + '-' + scale + '.out', 'w')
def presult(casenum, s):
    fpout.write('Case #' + str(casenum) + ': ' + s + '\n')



f = open(title + '-' + scale + '.in', 'r')


num_case = int(f.readline().rstrip())

for casen in range(1, num_case+1):
    pick1 = int(f.readline().rstrip())
    line1 = []
    for i in range(1, 5):
        line = f.readline().rstrip()
        if i == pick1:
            line1 = line.split(' ')
    pick2 = int(f.readline().rstrip())
    line2 = []
    for j in range(1, 5):
        line = f.readline().rstrip()
        if j == pick2:
            line2 = line.split(' ')

    result = list(set(line1).intersection(set(line2)))

    print(result)
    
    l = len(result)
    if l == 0:
        presult(casen, 'Volunteer cheated!');
    elif l > 1:
        presult(casen, 'Bad magician!');
    else:
        presult(casen, result[0])


