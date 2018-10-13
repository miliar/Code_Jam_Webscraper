# coding: utf-8

def solve_problem(digits):
    people_standing = 0
    result = 0
    for shyness, quantity in enumerate(digits):
        if shyness > people_standing:
            people_added = shyness - people_standing
            people_standing += people_added
            result += people_added
        people_standing += int(quantity)
    return result
    

with open('input_A.in') as input_file, open('output_A.out', 'w') as output_file:
    number_of_test_cases = int(input_file.readline())
    for i in range(number_of_test_cases):
        digits = input_file.readline().split(' ')[1].strip()
        result = solve_problem(digits)
        output_file.write('Case #{case_number}: {result}\n'.format(
            case_number=i+1,
            result=result,
        ))
