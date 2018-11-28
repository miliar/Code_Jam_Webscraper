import fileinput

num_inputs = 0
lines = []

for line in fileinput.input():
    lines.append(line)

num_inputs = int(lines[0])
for i in range(num_inputs):
    #get input
    index = 1 + 10*i
    first_answer = int(lines[index])
    first_rows = []
    for j in range(4):
        first_rows.append(lines[index+j+1].strip().split(' '))
    
    second_answer = int(lines[index+5])
    second_rows = []
    for j in range(4):
        second_rows.append(lines[index+j+6].strip().split(' '))

    first_row = []
    second_row = []

    for c in first_rows[first_answer-1]:
        first_row.append(c)

    for c in second_rows[second_answer-1]:
        second_row.append(c)

    possible_values = list(set(first_row).intersection(set(second_row)))

    if len(possible_values) > 1:
        print('Case #'+str(i+1)+': Bad magician!')
    elif len(possible_values) == 0:
        print('Case #'+str(i+1)+': Volunteer cheated!')
    else:
        print('Case #'+str(i+1)+': '+possible_values[0])

'''
    print('Case: '+str(i))
    print(first_rows)
    print(second_rows)
    print(first_rows[first_answer-1])
    print(second_rows[second_answer-1])
    print(possible_values)
    print(possible_values)
'''
