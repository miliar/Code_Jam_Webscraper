import sys
import math

def is_palindrome(number):
    number_str = str(number)
    if len(number_str) == 1: return True
    middle_index = len(number_str)//2
    return number_str[:middle_index] == number_str[-middle_index:][::-1]

def find_palindromes(min, max):
    palindromes = []
    min = int(min)
    max = int(max)
    while min < 10 and min <= max:
        palindromes.append(str(min))
        min += 1
    min_str = str(min)
    max_str = str(max)
    left = min_str[:len(min_str)//2]
    # find the 1st palindrome:
    palindrome = left + ((min_str[(len(min_str)//2)]) if len(min_str)%2 == 1 else '') + left[::-1]
    while (int(palindrome) <= max):
        # the first palindrome may be < min:
        if int(palindrome) >= min: palindromes.append(palindrome)
        # find the next palindrome:
        left = palindrome[:len(palindrome)//2]
        if len(palindrome)%2 == 1:  #odd number of digits
            middle = palindrome[len(palindrome)//2]
            if (int(middle) < 9):
                palindrome = left + str(int(middle)+1) + left[::-1]
            else:
                next_left = str(int(left) + 1)
                palindrome = next_left + ('0' if len(next_left) == len(left) else '') + next_left[::-1]
        else:  #even number of digits
            next_left = str(int(left) + 1)
            palindrome = next_left + ('0' if len(next_left) != len(left) else '') + next_left[::-1]
    return [int(x) for x in palindromes]

def find_fair_and_square(min, max):
    min_root = math.sqrt(min)
    max_root = math.sqrt(max)
    root_palindromes = find_palindromes(min_root, max_root)
    #print(root_palindromes)
    fair_and_squares = []
    for palindrome in root_palindromes:
        palindrome_square = palindrome ** 2
        if is_palindrome(palindrome_square) and palindrome_square >= min and palindrome_square <= max:
            fair_and_squares.append(palindrome_square)
    return fair_and_squares

def main(input_file_name, output_file_name):
    input_file = open(input_file_name, 'rU')
    output_file = open(output_file_name, 'w')
    for i in range(int(input_file.readline())):
        min, max = (int(x) for x in input_file.readline().split())
        fair_squares = find_fair_and_square(min, max)
        output_file.write('Case #' + str(i+1) + ': ' + str(len(fair_squares)) + '\n')
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
