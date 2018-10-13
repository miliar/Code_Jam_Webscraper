import sys


def read_file(file_name='problem_a_test.txt'):
    with open(file_name, 'r') as in_file:
        in_file.readline()
        case_list = []
        for line in in_file:
            (_, audience) = line.split()            
            audience = map(int, list(audience))
            case_list.append(audience)
        return case_list


def write_file(solution, file_name='output_a_test.txt'):
    with open(file_name, 'w') as out_file:
        for idx, case in enumerate(solution):
            out_file.write('Case #{index}: {sol}\n'.format(index=idx+1, sol=case))
        

def solver(case):
    invite = 0
    accum = 0    
    for s_lvl, aud_lvl in enumerate(case):        
        if accum >= s_lvl:
            accum += aud_lvl
        else:
            accum += 1 + aud_lvl
            invite += 1
    return invite

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise ValueError('Wrong arguments! Usage: script input_file output_file')

    case_list = read_file(file_name=sys.argv[1])
    output = []
    
    for case in case_list:
        output.append(solver(case))

    write_file(output, file_name=sys.argv[2])







