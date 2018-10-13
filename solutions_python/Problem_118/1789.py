from math import sqrt

__author__ = 'tmehta'

file = open('C-small-attempt0.in', 'r')
out = open('output_fair.txt', 'w')
number_of_cases = file.readline()
lines = file.readlines()
output = ""


def isPalindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False


def get_number_of(line):
    if line[-1] == "\n":
        line = line[:-1]
    numbers = [int(x) for x in line.split(" ")]
    squares = []
    for x in range(int(sqrt(numbers[0])), int(sqrt(numbers[1])) + 1):
        squares.append(x * x if isPalindrome(x) else 0)
    squares = filter(lambda x: x != 0 and numbers[0] <= x <= numbers[1], squares)
    squares_and_palindrome = filter(lambda x: isPalindrome(x), squares)
    return str(len(squares_and_palindrome))

for i in range(int(number_of_cases)):
    number = get_number_of(lines[i])
    output += "Case #" + str(i + 1) + ": " + number + "\n"

out.write(output)
