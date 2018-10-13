import sys

def reading_the_file(input_file):
    f = open(input_file, 'r+')
    return f

def getting_test_cases(f):
    y0 = []
    for counter, line in enumerate(f):
        case = counter + 1
        if counter == 0:
            number_of_test_cases = line
            continue
        if counter > 0:
            y0.append(line[:-1])
    return {'C':[x for x in y0], 'cases' : int(number_of_test_cases) }

def going_through_the_cases(C,cases):
    output_file_name = sys.argv[1][:-2]+'out'
    with open(output_file_name, 'w') as f:
        for i in range(cases):
            result = algorithm(C[i])
            f.write('Case #{}'.format(i+1)+': '+ result)


def algorithm(C):
    place_of_same_digit_seq = -1
    place_of_decrease = -1
    the_repeating_digit = -1
    digit_from_decrease = -1
    num = [int(i) for i in C]  
    digit_to_compare_to = num[0]
    if len(C) > 1:  
        for i in range(1,len(C)): 
            if num[i] < digit_to_compare_to:
                place_of_decrease = i - 1  
                digit_from_decrease = num[i - 1]
                break
            elif num[i] == digit_to_compare_to: 
                if place_of_same_digit_seq == -1:
                    place_of_same_digit_seq = i - 1
                    the_repeating_digit = num[i - 1]
            else:
                place_of_same_digit_seq = -1
            digit_to_compare_to = num[i]
        if place_of_decrease == -1:
            Tidy_num = ''.join([str(x) for x in num]) + '\n'
        elif digit_from_decrease == 1:
            Tidy_num = '9'*(len(C) - 1) + '\n'
        else:
            if place_of_same_digit_seq == -1:
                Tidy_num = C[0:place_of_decrease] + str(digit_from_decrease - 1) + '9'*(len(C)- 1 - place_of_decrease) + '\n'
            else:
                Tidy_num = C[0:place_of_same_digit_seq] + str(digit_from_decrease - 1) + '9'*(len(C)- 1 - place_of_same_digit_seq) + '\n'
    else:
        Tidy_num = ''.join([str(x) for x in num]) + '\n'
    return Tidy_num

def main():
    input_file = sys.argv[1]
    going_through_the_cases(**getting_test_cases(reading_the_file(input_file)))

if __name__ == '__main__':
    main()

