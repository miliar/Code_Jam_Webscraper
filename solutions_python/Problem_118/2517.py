#Fair and Square - Small
import math

def is_palindrome(number):
    nbr_cpy = number
    result_nbr = 0
    while nbr_cpy != 0:
        result_nbr *= 10
        result_nbr += nbr_cpy % 10
        nbr_cpy /= 10

    return True if result_nbr == number else False

def is_fair_and_square(number):
    if(is_palindrome(number) == False):
        return False
    sqrt_number = int(math.sqrt(number))
    if(sqrt_number ** 2 != number):
        return False
    if(is_palindrome(sqrt_number) == False):
        return False
    return True

def fair_and_square(element):
    result = 0
    for i in range(element[0], element[1] + 1):
        if is_fair_and_square(i):
            result += 1
    return result

input_file = open('C-small-attempt3.in', 'rU')

test_cases = int(input_file.readline().rstrip())
cases = []

for i in range(0, test_cases):
    cases.append(tuple([int(x) for x in input_file.readline().rstrip().split(' ')]))

input_file.close()

string_output = "Case #%d: %d\n"
results = map(fair_and_square, cases)

output_file = open('output3.out', 'w')
for i in range(0, len(results)):
    output_file.write(string_output % (i + 1, results[i]))
output_file.close()
