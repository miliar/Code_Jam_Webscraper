file_in = open('in2.txt', 'r')
file_out = open('out2.txt', 'w')

case_number = int(file_in.readline())

dic = dict()

dic['1'] = {
    '1': '1',
    'i': 'i',
    'j': 'j',
    'k': 'k'
}

dic['i'] = {
    '1': 'i',
    'i': '-1',
    'j': 'k',
    'k': '-j'
}

dic['j'] = {
    '1': 'j',
    'i': '-k',
    'j': '-1',
    'k': 'i'
}

dic['k'] = {
    '1': 'k',
    'i': 'j',
    'j': '-i',
    'k': '-1'
}

dic['-1'] = {
    '1': '-1',
    'i': '-i',
    'j': '-j',
    'k': '-k'
}

dic['-i'] = {
    '1': '-i',
    'i': '1',
    'j': '-k',
    'k': 'j'
}

dic['-j'] = {
    '1': '-j',
    'i': 'k',
    'j': '1',
    'k': '-i'
}

dic['-k'] = {
    '1': '-k',
    'i': '-j',
    'j': 'i',
    'k': '1'
}

target = ['i', 'j', 'k']


for i in range(case_number):
    case_size, case_repeat = [int(x) for x in file_in.readline().split()]

    case_input = file_in.readline()
    if case_input[-1] == '\n':
        case_input = case_input[:-1]

    case_input *= case_repeat

    current = case_input[0]
    target_index = 0
    
    for j in range(1, len(case_input)):        
        if target_index < 3 and current[-1] == target[target_index]:
            target_index += 1

            if current[0] == '-':
                current = '-1'
            else:
                current = '1'

        
        current = dic[current][case_input[j]]

    if target_index < 3 and current[-1] == target[target_index]:
        target_index += 1
        
        if current[0] == '-':
            current = '-1'
        else:
            current = '1'

    if target_index == 3 and current == '1':
        result = 'YES'
    else:
        result = 'NO'

    file_out.write('Case #{}: {}\n'.format(i + 1, result))
    print(result)


file_in.close()
file_out.close()
