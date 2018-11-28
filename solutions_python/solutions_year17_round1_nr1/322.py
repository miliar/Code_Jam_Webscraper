input_file = open("input.in", 'r')
output_file = open("output.out", 'w')

def file_input():
    input_string = input_file.readline()
    if input_string[-1] == '\n':
        input_string = input_string[:-1]
    return input_string

def make_col(listy, rows, col):
    ch = '?'
    for i in range(rows):
        if listy[i][col] == '?':
            listy[i][col] = ch
        else:
            ch = listy[i][col]
    ch = '?'
    for i in range(rows - 1, -1, -1):
        if listy[i][col] == '?':
            listy[i][col] = ch
        else:
            ch = listy[i][col]
        
    return listy

def copy_col(listy, rows, col1, col2):
    for i in range(rows):
        listy[i][col1] = listy[i][col2]
    return listy

testcases = int(file_input())

for x in range(1, testcases + 1):
    row, col = file_input().split()
    row = int(row)
    col = int(col)
    temp = []
    listy = []
    for i in range(row):
        temp.append(file_input())
        listy.append([])
        for j in temp[-1]:
            listy[-1].append(j)

    for i in range(col):
        listy = make_col(listy, row, i)

    for i in range(col):
        if listy[0][i] == '?':
            if i != 0:
                if listy[0][i-1] != '?':
                    listy = copy_col(listy, row, i, i-1)
    for i in range(col - 1, -1, -1):
        if listy[0][i] == '?':
            listy = copy_col(listy, row, i, i+1)


    output_file.write("Case #" + str(x) + ":\n")
    for i in listy:
        for j in i:
            output_file.write(j)
        output_file.write('\n')
    
input_file.close()
output_file.close()
