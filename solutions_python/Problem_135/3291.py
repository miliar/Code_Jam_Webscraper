9
#!/usr/bin/python

def read_board(row_number):
    for i in xrange(4):
        if i + 1 == row_number:
            row = map(int, raw_input().split(' '))
        else:
            raw_input()    
    return row 

ncases = int(raw_input())

for ncase in xrange(ncases):
    first_row_number = int(raw_input())
    first_row = read_board(first_row_number)

    second_row_number = int(raw_input())
    second_row = read_board(second_row_number)
    match_count = 0
    number = 0
    for i in first_row:
        for j in second_row:
            if i == j:
                number = i
                match_count += 1
                break

    answer = 'Case #' + str(ncase + 1) + ': '
    if match_count == 0:
        print answer + 'Volunteer cheated!'
    elif match_count == 1:
        print answer + str(number)
    else:
        print answer + 'Bad magician!'    
    
