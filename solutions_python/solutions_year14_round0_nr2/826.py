import sys
from math import ceil

def solve_case(case_num, case_data):
    result = 'Case #' + str(case_num) + ': '
    R = 2.0
    C = case_data[0]    ## Cost of farm
    F = case_data[1]    ## Farm rate
    X = case_data[2]    ## Target

    ## Solve optimal number of farms
    farms = int(ceil((X-C) / C - R/F))
    if farms < 0:
        farms = 0
    
    ## Calculate time
    time = 0
    for i in range(farms):
        time += C / (R + i*F)

    time += X / (R + farms * F)
    result += ('%.7f' % time)
    return result


def process_file(input_file, output_file):
    file_in = open(input_file, 'rU')
    file_out = open(output_file, 'w')

    i = 0
    num_cases = None
    case_num = 0

    for row in file_in:
        
        if not num_cases:
            num_cases = int(row)

        else:
            case_num += 1
            case_data = [float(n) for n in (row.strip()).split(' ')]
            result = solve_case(case_num, case_data)
            file_out.write(result+'\n')

        i += 1
        
    file_out.close()
            

def main():
    if len(sys.argv) == 3:
        print 'Program starts'
        process_file(sys.argv[1], sys.argv[2])
        sys.exit(1)
        
    else:
        print 'Give two arguments (INPUT_FILE OUTPUT_FILE)'
        sys.exit(1)


if __name__ == '__main__':
    main()
