import sys
import numpy as np

def solve_case(case_num, case_data):
    result = 'Case #' + str(case_num) + ': '

    w1 = sorted(case_data[0])
    w2 = sorted(case_data[1])

    
    ken_used = []
    war_points = 0

    ## Play War
    for w in w1[::-1]:
        ken_possible = [x for x in range(len(w2)) if (w2[x] > w and x not in ken_used)]
        if len(ken_possible) > 0:
            i_ken = min(ken_possible)
        else:
            war_points += 1
            i_ken = min([x for x in range(len(w2)) if x not in ken_used])
        ken_used.append(i_ken)            


    ## Play Deceitful War
    deceitful_points = 0
    while len(w1) > 0:
        if w1[0] < w2[0]:
            del w1[0]
            del w2[-1]
        else:
            del w1[0]
            del w2[0]
            deceitful_points += 1
            
    result += str(deceitful_points) + ' ' + str(war_points)
    return result


def process_file(input_file, output_file):
    file_in = open(input_file, 'rU')
    file_out = open(output_file, 'w')

    i = 0
    num_cases = None
    case_num = 0
    case_data = None

    for row in file_in:
        
        if not num_cases:
            num_cases = int(row)

        elif i == 0:
            case_num += 1
            i += 1
            case_data = []

        elif i == 1:
            i += 1
            case_data.append([float(n) for n in (row.strip()).split(' ')])

        elif i == 2:
            case_data.append([float(n) for n in (row.strip()).split(' ')])
            result = solve_case(case_num, case_data)
            file_out.write(result+'\n')
            i = 0
        
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
