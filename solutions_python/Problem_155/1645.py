inputF = open('A-large.in', 'r')
output = open('A-large.out', 'w')

numCases = int(inputF.readline())

for i in range(numCases):
    line = inputF.readline()
    n = int(line.split()[0])
    string = line.split()[1]
    standing = 0
    added = 0
    for j in range(n+1):
        if j >= standing and int(string[j]) == 0:
            added += 1
            standing += 1
        else:
            standing += int(string[j])

    output.write('Case #' + str(i+1) + ': ')
    output.write(str(added) + '\n')




inputF.close()
output.close()
