infile = open('B-large.in','r')
outfile = open('outB.txt','w')

def possible(lawn,num):
    row_max = []
    column_max = []
    for i in range(len(lawn)):
        row_max.append(0)
    for i in range(len(lawn[0])):
        column_max.append(0)
    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            if lawn[i][j] > row_max[i]:
                row_max[i] = lawn[i][j]
    for i in range(len(lawn[0])):
        for j in range(len(lawn)):
            if lawn[j][i] > column_max[i]:
                column_max[i] = lawn[j][i]
    if num >= 0:
        for i in row_max:
            print i
        print ''
        for i in column_max:
            print i
        print ''
    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            if (not lawn[i][j] == row_max[i]) and (not lawn[i][j] == column_max[j]):
                return 'NO'
    return 'YES'
        

num_cases = int(infile.readline())

for i in range(num_cases):
    lawn = []
    lawn_size = infile.readline()
    lawn_size = lawn_size.split()
    height = int(lawn_size[0])
    width = int(lawn_size[1])
    for j in range(height):
        lawn.append(infile.readline().split())
    for j in range(len(lawn)):
        for k in range(len(lawn[j])):
            lawn[j][k] = int(lawn[j][k])
    outfile.write('Case #' + str(i + 1) + ': ' + possible(lawn,i) + '\n')
outfile.close()
infile.close()
    