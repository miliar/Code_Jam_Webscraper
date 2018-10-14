import sys


def solve_case(case_no, case_input):

    data_arr = case_input.strip().split(' ')
    data = data_arr[1]
    
    invitations = 0
    clappers = 0
    for i in range(len(data)):
        x = int(data[i])
        if clappers >= i:
            clappers += x
        else:
            invite = i - clappers
            invitations += invite
            clappers += invite
            clappers += x
    res = ('Case #%i: %i' % (case_no, invitations))
    ##print(res)
    return res

def process_file(input_file, output_file):
    file_in = open(input_file, 'rU')
    file_out = open(output_file, 'w')

    
    num_cases = None
    case_num = 0

    for row in file_in:
        
        if not num_cases:
            num_cases = int(row)

        else:
            case_num += 1
            result = solve_case(case_num, row.rstrip())
            file_out.write(result + '\n')
        
    file_out.close()
            

def main():
    if len(sys.argv) == 3:
        print('Program starts')
        process_file(sys.argv[1], sys.argv[2])
        sys.exit(1)
        
    else:
        print('Give two arguments (INPUT_FILE OUTPUT_FILE)')
        sys.exit(1)


if __name__ == '__main__':
    main()
