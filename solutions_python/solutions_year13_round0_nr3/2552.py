import sys
import math


def isPalindrome(number):
    number = str(number)
    mid = len(number) / 2
    half1 = number[0:mid]
    if len(number) % 2 == 0:
        half2 = number[mid:]
    else:
        half2 = number[mid + 1:]
    half2 = half2[::-1]
    if half1 == half2:
        return True
    else:
        return False


def isSquare(number):
    root = math.sqrt(number)
    if root == float(int(root)):
        return True
    else:
        return False


def rootIsPalindrome(number, palindromes):
    root = int(math.sqrt(number))
    if root in palindromes:
        return True
    else:
        return False


def get_numbers(input):
    limits = list(input.next().split())
    start = int(limits[0])
    end = int(limits[1]) + 1
    return (start, end)


def find_fair_and_square(numbers):
    output = 0
    palindromes = []
    for number in range(0, numbers[0]):
        if isPalindrome(number):
            palindromes.append(number)
    for number in range(numbers[0], numbers[1]):
        if isPalindrome(number):
            palindromes.append(number)
            if isSquare(number) and rootIsPalindrome(number, palindromes):
                output += 1
    return output

input = open(sys.argv[1], 'r')

num_tests = int(input.readline())

for case in range(1, num_tests + 1):
    numbers = get_numbers(input)
    outcome = find_fair_and_square(numbers)
    message = "Case #{case}: {outcome}".format(case=case, outcome=outcome)
    print(message)
