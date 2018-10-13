file = open('input.txt')

output_file = open('output.txt', 'w')

test_cases = int(file.readline())


for tc in range(1,test_cases + 1):
    row_with_card = int(file.readline())
    for i in range(1,5):
        row = file.readline()
        if row_with_card == i:
            first = row.split()

    second_row_with_card = int(file.readline())
    for i in range(1,5):
        row = file.readline()
        if second_row_with_card == i:
            second = row.split()
    
    intersection = list(set(first) & set(second))
    
    if len(intersection) == 0:
        result = 'Volunteer cheated!'
    elif len(intersection) == 1:
        result = intersection[0]
    else:
        result = 'Bad magician!'
    
    print('Case #',tc,': ',result, sep="")
    output_file.write('Case #' + str(tc) + ': ' + str(result) + '\n')