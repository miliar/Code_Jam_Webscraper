from math import sqrt
from math import ceil
from math import floor

def is_palindrome(number):
    string_number = str(number)
    halfway = len(string_number) // 2
    palindrome = True
    for i in range(halfway):
        if (string_number[i] != string_number[len(string_number) - (i + 1)]):
            palindrome = False
    return(palindrome)

def is_square(number):
    return(sqrt(number).is_integer())

def find_number(bottom, top):
    number = 0
    least_square = ceil(sqrt(bottom))
    most_square = floor(sqrt(top))
    for i in range(least_square, (most_square + 1)):
        if (is_palindrome(i) and is_palindrome(i ** 2)):
            number += 1
    return number
	
def solve(input):
    split_input = input.split(" ")
    low = int(split_input[0])
    number = find_number(low,int(split_input[1])) 
    return(number)
	
def process_tests(command_to_run):
    in_file = open('in')
    out_file = open("out","w")
    number_of_tests = int(in_file.readline())
    for test_case in range(number_of_tests):
        test_string = in_file.readline()[:-1]
        test_answer = command_to_run(test_string)
        out_file.write("Case #" + str(test_case + 1) + ": " + str(test_answer) + "\n")
    out_file.close()
    in_file.close()
	
	
process_tests(solve)