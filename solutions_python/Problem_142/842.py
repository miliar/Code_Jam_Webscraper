import ProblemFileIO

def main():
    filename = 'A-small-attempt2'
    ProblemIO = ProblemFileIO.ProblemFileIO(filename, case_function)
    for (number_of_strings, string_list) in ProblemIO.case_generator():
        result = solve(number_of_strings, string_list)
        ProblemIO.write_result(result)

def case_function(file_object):
    number_of_strings = ProblemFileIO.read_int(file_object)
    string_list = []
    for i in xrange(number_of_strings):
        problem_string = ProblemFileIO.read_string(file_object)
        string_list.append(problem_string)
    return (number_of_strings, tuple(string_list))
            
def solve(number_of_strings, string_list):
    if (number_of_strings == 1):
        return "0"
    reference_string = string_list[0]
    number_of_actions = 0
     
    start_indices = [0] * number_of_strings
    number_of_found_chars = [0] * number_of_strings
    
    
    while (True):
        reference_char = reference_string[start_indices[0]]
        sum_of_found_chars = 0
        for string_index in xrange(number_of_strings):
            number_of_chars = count_char_number(string_list[string_index], start_indices[string_index], reference_char)
            if (0 == number_of_chars):
                return "Fegla Won"
            number_of_found_chars[string_index] = number_of_chars
            start_indices[string_index] += number_of_chars
            sum_of_found_chars += number_of_chars

        print number_of_found_chars

        mean_of_found_chars = round(1.0 * (float(sum_of_found_chars) / number_of_strings))

        for string_index in xrange(number_of_strings):
            actions_to_add = abs(mean_of_found_chars - number_of_found_chars[string_index])
            number_of_actions += actions_to_add
        if (start_indices[0] == len(reference_string)):
            break
        
    for string_index in xrange(number_of_strings):
        if (start_indices[string_index] < len(string_list[string_index])):
            return "Fegla Won"

            
    return "%d" %number_of_actions
    
def count_char_number(input_string, start_index, char_to_count):
    counter = 0
    for char_index in xrange(len(input_string)-start_index):
        char_index += start_index
        
        if (char_to_count == input_string[char_index]):
            counter = counter + 1
        else:
            break

    return counter

if __name__ == '__main__':
    main()