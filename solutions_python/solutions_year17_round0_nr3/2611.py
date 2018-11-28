import sys
from math import floor

def solve(N, K):

    full_stalls = [0, N+1]
    for i in range(K):
        gap_min = -1
        gap_max = -1
        ind = None
        ind_j = None
        for j in range(1, len(full_stalls)):
            l = full_stalls[j-1]
            r = full_stalls[j]
            pos = l + floor((r - l) / 2.)
            gap_l = pos - l - 1
            gap_r = r - pos - 1
            curr_min = min(gap_l, gap_r)
            curr_max = max(gap_l, gap_r)
            if curr_min > gap_min:
                gap_min = curr_min
                gap_max = curr_max
                ind = int(pos)
                ind_j = j
            elif curr_min == gap_min and curr_max > gap_max:
                gap_min = curr_min
                gap_max = curr_max
                ind = int(pos)
                ind_j = j
        full_stalls.insert(ind_j, ind)


    return gap_max, gap_min




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
            row_split = row.split(' ')
            gap_max, gap_min = solve(int(row_split[0]), int(row_split[1]))
            res_string = 'Case #%i: %i %i' % (case_num, gap_max, gap_min)
            print(res_string)
            file_out.write(res_string + '\n')

    file_out.close()
            

def main():
    if len(sys.argv) == 3:
        print('Program starts')
        process_file(sys.argv[1], sys.argv[2])
        print('Done')
        sys.exit(1)
        
    else:
        print('Give two arguments (INPUT_FILE OUTPUT_FILE)')
        sys.exit(1)


if __name__ == '__main__':
    main()
