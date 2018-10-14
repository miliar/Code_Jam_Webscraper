import pdb
quaternion_multiplication = {
    'ii': '-1', 'ij': 'k' , 'ik': '-j',
    'ji': '-k', 'jj': '-1', 'jk': 'i' ,
    'ki': 'j' , 'kj': '-i', 'kk': '-1',
}


def getInput(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines


def get_solution():
    if validate(0, ['i', 'j', 'k']) is False:
        return "NO"
    i_ignore = 0
    j_ignore = 0
    run_i = True
    while True:
        if run_i is True:
            if i_ignore > 0:
                i_found, i_end_index = search_for_char(i_end_index+1, '1', 0)
            else:
                i_found, i_end_index = search_for_char(0, 'i', 0)
            if i_found is False:
                return "NO"
            j_start_index = i_end_index + 1
            if j_start_index >= total_len:
                return "NO"
        if validate(j_start_index, ['j', 'k']) is False:
            return "NO"

        if j_ignore > 0:
            j_found, j_end_index = search_for_char(j_end_index+1, 'j', 0)
        else:
            j_found, j_end_index = search_for_char(j_start_index, 'j', 0)
        if j_found is False:
            i_ignore += 1
            j_ignore = 0
            run_i = True
        else:
            return "YES"
            """
            k_start_index = j_end_index + 1
            k_found, k_end_index = search_for_char(k_start_index, 'k', 0)
            if k_start_index >= total_len:
                return "NO"
            if k_found is False:
                j_ignore += 1
                run_i = False
            else:
                if k_end_index + 1 == total_len:
                    return "YES"; #print i_end_index, j_end_index
                else:
                    j_ignore += 1
                    run_i = False
            """

   
def validate(from_index, chars_to_find):
    unique_dict = {}
    product = '1'
    for index in xrange(total_len):
        char = input_string[index%len(input_string)]
        unique_dict[char] = 1
        product = multiply(product, char)
    if len(unique_dict) == 1:
        if len(chars_to_find) == 1 and unique_dict.keys()[0] != chars_to_find[0]:
            return False
        if len(chars_to_find) == [2, 3]:
            return False
    if len(chars_to_find) == 3 and product != '-1':
        return False
    return True

"""
char_to_find - The character to search
ignore_count - Ignore the first ignore_count occurances
"""
def search_for_char(from_index, char_to_find, ignore_count):
    if validate(from_index, [char_to_find]) is False:
        return False, -1
    product = '1'
    solution_count = 0
    for index in xrange(from_index, total_len):
        char = input_string[index%len(input_string)]
        product = multiply(product, char)
        if product == char_to_find:
            solution_count += 1
            if ignore_count < solution_count:
                return True, index
    return False, -1


def multiply(first_input, second_input):
    end_multiplier = 1
    if first_input.startswith("-"):
        first_input = first_input[1:]
        end_multiplier *= -1
    if second_input.startswith("-"):
        second_input = second_input[1:]
        end_multiplier *= -1
    if first_input == '1':
        return second_input if end_multiplier is 1 else "-"+second_input
    if second_input == '1':
        return first_input if end_multiplier is 1 else "-"+first_input
    product = quaternion_multiplication[first_input+second_input]
    if product.startswith("-"):
        end_multiplier *= -1
        product = product[1:]
    return product if end_multiplier is 1 else "-"+product


if True:
    lines = getInput("inputC.txt")
    no_cases = int(lines[0].strip())
    case = 1
    while (case<=no_cases):
        line_no = case*2 -1
        L, X = [int(y) for y in lines[line_no].strip().split()]
        input_string = lines[line_no+1].strip()
        total_len = X * len(input_string)
        sol = get_solution()
        print "Case #{0}: {1}".format(case, sol)
        case  += 1


