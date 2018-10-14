f_input  = open('d:\gjam\A-small-attempt0.in', 'r')
f_output = open('d:\gjam\magic_output.txt', 'w')

n_test = int(f_input.readline())

for i in range(n_test):
    num_row_1 = int(f_input.readline()) - 1
    row_1 = []
    for k in range(4):
        t = f_input.readline()
        if (k == num_row_1):
            row_1 = map(int, t.split(' '))
    num_row_2 = int(f_input.readline()) - 1
    row_2 = []
    for k in range(4):
        t = f_input.readline()
        if (k == num_row_2):
            row_2 = map(int, t.split(' '))    

    intersect = list(set(row_1).intersection(set(row_2)))
    #print(row_1, row_2, intersect)
    if (len(intersect) == 0):
        f_output.write('Case #' + str(i+1) + ': Volunteer cheated!\n')
    elif (len(intersect) > 1):
        f_output.write('Case #' + str(i+1) + ': Bad magician!\n')
    else:
        f_output.write('Case #' + str(i+1) + ': ' + str(intersect[0]) + '\n')

f_input.close()
f_output.close()
