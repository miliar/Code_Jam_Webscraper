#!env python

def get_intersection(first_row, second_row):
    first_row_int = [int(x) for x in first_row.split(' ')]
    second_row_int = [int(x) for x in second_row.split(' ')]
    return list(set(first_row_int) & set(second_row_int))

in_f = open('input', mode='r')
in_lines = in_f.readlines()
num_cases = int(in_lines[0].strip())

for i in range(0, num_cases):
    first_choice = int(in_lines[1 + i*10].strip())
    first_row = in_lines[1 + i*10 + 1 + first_choice - 1].strip()
    second_choice = int(in_lines[1 + i*10 + 5].strip())
    second_row = in_lines[1 + i*10 + 1 + 5 + second_choice - 1].strip()
    intersection = get_intersection(first_row, second_row)
    print "Case #%d: " % (i+1),
    if len(intersection) == 1:
        print intersection[0]
    elif len(intersection) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"
