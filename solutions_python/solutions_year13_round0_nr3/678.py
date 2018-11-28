#!/usr/bin/env python
import math, itertools

def generate_palindromes():
    palindromes_by_length = {}
    for length in itertools.count(1):
        palindromes_by_length[length] = []
        if length > 2:
            for c in "012":  # from testing, the only palindromes we actually want are composed entirely of 0s, 1s, and 2s
                for inner_palindrome in palindromes_by_length[length-2]:
                    palindrome = "{0}{1}{0}".format(c, inner_palindrome)
                    yield palindrome
                    palindromes_by_length[length].append(palindrome)
        else:
            for c in "0123456789":
                palindrome = "".join([c]*length)
                yield palindrome
                palindromes_by_length[length].append(palindrome)

def is_palindrome(word):
    for idx in range(math.ceil(len(word) / 2)):
        if word[idx] != word[-(idx+1)]:
            return False
    return True


def fair_and_square_palindromes(limit=10**14):
    raw_palindromes = itertools.takewhile((lambda x: int(x) < limit),
        generate_palindromes())  # all palindromes below 10**14
    palindromes = filter((lambda x: x[0] != "0"), raw_palindromes)  # remove false palindromes
    for palindrome in palindromes:
        if is_palindrome(str(int(palindrome) ** 2)):
            yield(int(palindrome) ** 2)  # yield only if the square is still a palindrome

def main():
    import sys
    all_fair_and_square = list(fair_and_square_palindromes())
    num_test_cases = int(next(sys.stdin).strip())
    for i in range(num_test_cases):
        min_palindrome, max_palindrome = map(int, next(sys.stdin).split())
        in_range = filter((lambda x: x >= min_palindrome and x <= max_palindrome),
                all_fair_and_square)
        sys.stdout.write("Case #{0}: {1}\n".format(i+1, len(list(in_range))))

if __name__ == "__main__":
    main()
