import os
import sys
import math

"""
The basic code for reading a file, should return a string
"""
def parse_input(input_file):
    f = open(input_file, "r")
    test_cases = int(f.readline())
    final_string = ""
    for i in range(test_cases):
        params = f.readline().split()
        A = int(params[0])
        B = int(params[1])
        current = int(math.sqrt(A)) - 1
        square = current ** 2
        count = 0
        while square <= B:
            square = current ** 2
            if is_palindrome(square) and is_palindrome(current) and square <= B and square >= A:
                count = count + 1
            current = current + 1
        final_string = final_string + "Case #{0}: {1}\n".format(i+1, count)
    f.close()
    return final_string

def is_palindrome(number):
    num_string = str(number)
    high = len(num_string) - 1
    low = 0
    while high > low:
        if num_string[low] != num_string[high]:
            return False
        low = low + 1
        high = high - 1
    return True


"""
Writes a string to the file of the form X-Y-output.txt,
where X is the name of this script and Y is the name of the
test case
"""
def write_output(answer_string):
    script_name = os.path.splitext(sys.argv[0])[0] + "-"
    f = open("Outputs/" + script_name +"output.txt","w")
    f.write(answer_string)
    f.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        answer_string = parse_input(sys.argv[1])
        if answer_string == None:
            print "No answer given"
        else:
            write_output(answer_string)
    else:
        print "Pass in the input file"
