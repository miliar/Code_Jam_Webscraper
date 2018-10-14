import fileinput

state = 0
result = []
msg = 'Case #{test}: {msg}'
row_count = 1
chosen_row = None
possibilities = None
test_number = 0

for line in fileinput.input():
    # Number of tests
    if state == 0:
        state = 1
    # Question: Pick a row
    elif state == 1:
        chosen_row = int(line)
        row_count = 1
        state = 2
    # All rows
    elif state == 2:
        if chosen_row == row_count:
            p = line.split()
            if not possibilities:
                possibilities = p
            else:
                l = [x for x in p if x in possibilities]
                test_number += 1
                if len(l) == 0:
                    result.append(msg.format(test=test_number, msg='Volunteer cheated!'))
                elif len(l) == 1:
                    result.append(msg.format(test=test_number, msg=l[0]))
                else:
                    result.append(msg.format(test=test_number, msg='Bad magician!'))
                possibilities = None

            if row_count >= 4:
                state = 1
            else:
                state = 3
        row_count += 1

    elif state == 3:
        if row_count >= 4:
            state = 1
        row_count += 1

print '\n'.join(result)
