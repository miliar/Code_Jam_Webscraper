f = open('input.in', 'r')

nInput = int(f.readline())

nCase = 0

for line in f:
    nCase += 1
    line = line.replace('\n', '')
    line = (list(line))
    line_len = len(line)

    index = line_len - 1
    did_9_appear = False
    left_most_9_index = index

    while index-1 >= 0:
        if line[index] < line[index-1]:
            line[index] = '9'
            line[index-1] = str(int(line[index-1]) - 1)
            if ~did_9_appear:
                did_9_appear = True
            left_most_9_index = index
        index -= 1

    if did_9_appear:

        line[left_most_9_index:line_len] = ['9']*(line_len - left_most_9_index)

    if line[0] == '0':
        del line[0]

    print("Case #", end='')
    print(nCase, end='')
    print(": ", end='')
    print(''.join(line), end='\n')


f.close()

