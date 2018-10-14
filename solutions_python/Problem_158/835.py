import sys


def solve_case(case_no, data):

    data = data.split(' ')
    x = int(data[0])
    r = int(data[1])
    c = int(data[2])

    result = None
    area = r*c

    ## Spill
    if x > area:
        result = 'RICHARD'

    ## 1-by-x
    elif x > max(r, c):
        result = 'RICHARD'

    ## Isolate empty cell
    elif x >= 7:
        result = 'RICHARD'

    ## Division impossible
    elif area % x != 0:
        result = 'RICHARD'

    ## Doesn't fit
    elif round((x - 1) / 2, 0) + 1 > min(r, c):
        result = 'RICHARD'

    else:
        result = 'GABRIEL'
    
    
    res = ('Case #%i: %s' % (case_no, result))
    print(res)
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
            data = row.rstrip()
            result = solve_case(case_num, data)
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
