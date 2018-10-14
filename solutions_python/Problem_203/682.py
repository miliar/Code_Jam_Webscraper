def parse_input(matrix_as_array):
    str_vals = [list(str) for str in matrix_as_array]
    # good_list = [0 if]
    return str_vals

def solve(R,C,matrix_as_array):
    matrix = parse_input(matrix_as_array)

    # print(matrix)
    output_mat = []
    rows_empty = 0
    new_row = []

    mat_size = len(matrix)
    for ind,row in enumerate(matrix):
        # print("row:",row)
        non_void_chars = [ x for x in row if x is not '?' ]
        # print("non_void_chars:",non_void_chars)
        num_of_cap = len(non_void_chars)
        if num_of_cap == 0:
            rows_empty += 1
            if mat_size-1 == ind:
                new_mat = [new_row for i in xrange(rows_empty)]
                output_mat += new_mat

        elif num_of_cap == 1:
            # print("non_void_chars*C:",non_void_chars*C)
            new_row = (non_void_chars*C)
            new_mat = [new_row for i in xrange(rows_empty+1)]
            # print("new_mat 1:",new_mat)
            output_mat += new_mat
            rows_empty = 0
        else:
            new_row = ['a']*len(row)
            last_latter = non_void_chars[0]

            for i in xrange(len(row)):
                if row[i] != '?':
                    last_latter = row[i]
                new_row[i] = last_latter
            # print("new_row 2:",new_row)
            new_mat = [new_row for i in xrange(rows_empty+1)]
            # print("new_mat 2:",new_mat)
            output_mat += new_mat

            rows_empty = 0

    mat_as_string = ""
    # print("output_mat:",output_mat)
    for row in output_mat:
        # print("row:",row)
        line = ''.join(row)
        mat_as_string += line +'\n'

    return mat_as_string
    #
    # for person in range(0,num_of_persons):
    #     treeRoot.splitTree()
    #
    #
    # return map(str,[treeRoot.getNodeMin(),treeRoot.getNodeMax()])
