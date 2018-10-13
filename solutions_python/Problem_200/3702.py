def load_data(filename):
    with open(filename) as file_handle:
        content = file_handle.read().splitlines()
    
    num_cases = int(content[0])
    
    retval = []
    for idx in range(1, num_cases + 1):
        sample = int(content[idx])
        retval.append(sample)
    
    return retval

def is_tidy(number):
    num_string = "{}".format(number)
    
    right_digit = int(num_string[-1])
    
    for left_char in reversed(num_string):
        left_digit = int(left_char)
        if left_digit > right_digit:
            return False
        right_digit=left_digit
    
    return True


def is_tidy(number):
    num_string = "{}".format(number)
    
    right_digit = int(num_string[-1])
    
    for left_char in reversed(num_string):
        left_digit = int(left_char)
        if left_digit > right_digit:
            return False
        right_digit = left_digit
    
    return True


def skip_untidy(number):
    if is_tidy(number):
        return number
    
    num_string = "{}".format(number)
    
    num_zero = 1
    test_string = num_string[0:-num_zero]
    test_num = int(test_string)
    while (is_tidy(test_num) == False or is_tidy(test_num - 1) == False):
        num_zero += 1
        test_string = num_string[0:-num_zero]
        test_num = int(test_string)

    retval = "{}{}".format(test_string, '0' * num_zero)
    
#    print retval
    return retval
    
def get_last_tidy(number):
    retval = number
    retval = int(skip_untidy(number))

    while is_tidy(retval) == False:
        retval -= 1


    return retval

def main():
    #input_file = 'B-sample.in'
    input_file = 'B-large.in'
    #    input_file = 'round1-A-sample.txt'
    number_list = load_data(input_file)
    idx = 1;
    
    for number in number_list:
 #       print("{}".format(number))
        last_tidy = get_last_tidy(number)
        print("Case #{}: {}".format(idx, last_tidy))
        idx += 1


if __name__ == '__main__':
    main()
