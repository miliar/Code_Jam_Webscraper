def calc_snapper(first, second):
    n, k = int(first), int(second)
    v = (k % 2**n) == ((2**n)-1)
    if v:
        return 'ON'
    else:
        return 'OFF'

def read(line):
    return line.replace('\n', '').split(' ')

if __name__ == '__main__':
    
    input_problem = 'A'
    input_set = 'large'
    in_file = open('{}-{}.in'.format(input_problem, input_set), 'r')
    out_file = open('{}-{}.out'.format(input_problem, input_set), 'w')

    line = in_file.readline()

    i = 1
    for line in in_file:
        out_file.write('Case #{}: {}\n'.format(i, calc_snapper(*read(line))))
        i += 1

    in_file.close()
    out_file.close()

