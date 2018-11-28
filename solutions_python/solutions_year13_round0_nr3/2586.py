import math
import sys

def is_palindrome(number):
    return str(number)[::-1] == str(number)

def fair_and_square(x):
# fair and square number x means palindrome(sqrt(x)) && palindrome(x)
  fair = is_palindrome(x)
  square = math.sqrt(x) % 1 == 0.0 and is_palindrome(int(math.sqrt(x)))
  return fair and square

def fair_and_square_between(lower, upper):
    total = 0
    for i in xrange(lower, upper + 1):
        if fair_and_square(i):
            total += 1
    return total

def main():
    sys.stdin.readline() # throw away count
    for i, line in enumerate(sys.stdin):
        lower, upper = [int(x) for x in line.split(' ')]
        print "Case #{0}: {1}".format(i+1, fair_and_square_between(lower, upper))

main()
