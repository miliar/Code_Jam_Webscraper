import sys
from pprint import pprint

WIN_SITUATIONS = [
            (0,1,2,3),
            (4,5,6,7),
            (8,9,10,11),
            (12,13,14,15),

            (0,4,8,12),
            (1,5,9,13),
            (2,6,10,14),
            (3,7,11,15),

            (0,5,10,15),
            (3,6,9,12)
        ]


def transform_case_into_list(inp):
    # inp == ['xxxx', 'xxxx', 'xxxx', 'xxxx']
    t_map = {
            'O': 1,
            'X': -1,
            'T': 1,
            '.': 0
            }
    t_map2 = {
            'O': 1,
            'X': -1,
            'T': -1,
            '.': 0
            }

    A = list([t_map[x] for x in ''.join(inp)])
    B = list([t_map2[x] for x in ''.join(inp)])

    return [A, B]

def get_line(inp, X):
    return [inp[x] for x in X]

def get_lines_sum(inp, A, B):
    result_list = []
    for situation in WIN_SITUATIONS:
        
        """
        print 'A'
        pprint(get_line(A, situation))
        print 'B'
        pprint(get_line(B, situation))
        """

        a_result = sum(get_line(A, situation))
        b_result = sum(get_line(B, situation))
        result_list += [a_result, b_result]

    return result_list
        
    
    

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as fp:
        input_lines = fp.readlines()
        input_lines = [x.strip() for x in input_lines]

    case_num = int(input_lines[0])

    rest_cases = input_lines[1:]

    inp_cases = []
    for i in range(case_num):
        offset=4*i
        start=offset+i
        end=start+4
        inp_cases.append(rest_cases[start:end])

    #pprint(inp_cases)

    ## start dealing with

    for n,each_case in enumerate(inp_cases):
        result = [0,0] #O(4), X(-4)
        AB = transform_case_into_list(each_case)
        #pprint(get_lines_sum(each_case, *AB))
        line_sum = get_lines_sum(each_case, *AB)

        not_complete = 0

        if 4 in line_sum:
            result[0] = 1
        if -4 in line_sum:
            result[1] = 1
        if 0 in AB[0]:
            not_complete = 1

        result_title = ""

        if result == [1,0]:
            result_title = "O won"
        elif result == [0,1]:
            result_title = "X won"
        elif result == [0,0]:
            if not_complete:
                result_title = "Game has not completed"
            else:
                result_title = "Draw"




        case_title = "Case #{0}: {1}\n".format(n+1, result_title)
        sys.stdout.write(case_title)



    
