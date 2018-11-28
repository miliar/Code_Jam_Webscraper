from math import sqrt, floor
from string import digits
from itertools import permutations

def main():
    f = open("small_input.txt")
    cases = int(f.readline())
    case_num = 1

    for line in f:
        original = [int(n) for n in line.strip("\n").split()]
        data = [int(floor(sqrt(n))) for n in original]
        palindromes = [i + i[::1] for i in permutations(digits, len(str(data[1]))//2)]
        int_palindromes = range(10) + [int("".join(i)) for i in palindromes[1:]]
       
        count = 0
        for palindrome in int_palindromes:
            square_palindrome = palindrome**2

            if square_palindrome > original[1]:
                break

            if square_palindrome >= original[0] and is_palindrome(square_palindrome):
                count += 1

        print "Case #" + str(case_num) + ": " + str(count)
        case_num += 1

def is_palindrome(i):
    s = str(i)
    start, end = 0, len(s) - 1
    is_palindrome = True
    while (start < end):
        if (s[start] == s[end]):
            start += 1
            end -= 1
            continue
        else:
            is_palindrome = False
            break

    return is_palindrome

if __name__ == "__main__":
    main()
