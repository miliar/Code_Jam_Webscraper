def read_inputs(input_filename):
    cases = []
    with open(input_filename) as file:
        num_inputs = int(file.readline())
        for line in file:
            cases.append(int(line)) 
    print(cases)
    return cases

def read_inputs2():
    t = int(input())  # read a line with a single integer
    case_set = []
    for i in range(1, t + 1):
        n = [int(s) for s in input()]  # read a list of integers, 2 in this case
        case_set.append(
            int(''.join(str(i) for i in n))
            )
    return case_set

def evaluate_tidy(number):
    if number < 10:
        return True

    while number > 10:
        last = number%10
        second_last = int(number%100/10)
        if last >= second_last:
            number = int(number/10)
            continue
        else:
            return False 
    return True

def skip_w_zeroes(number):
    str_number = str(number)

    if not '0' in str_number:
        return number

    while '0' in str(str_number):

        first_zero = str_number.index('0')
        
        before_zero = str_number[:first_zero]
        before_zero = before_zero[:-1] + str(
                                            int(before_zero[-1]) -1
                                        )
        str_number = before_zero + '9'*(len(str_number) - len(before_zero))
        str_number = str( int(str_number) )

    return int(str_number)

def print_output(results):
    for i in range(len(results)):
        print('Case #{0}: {1}'.format(i+1, results[i]))


input_filename = 'data/B-small-attempt1.in'
# cases = read_inputs(input_filename)
cases = read_inputs2()

result_set = []

for case in cases:
    
    number = case

    while number > 0:
        number = skip_w_zeroes(number)
        
        if evaluate_tidy(number):
            result_set.append(number)
            break
        number  -= 1
    
print_output(result_set)