#############
# Google Code Jam 2013
# by Jos Kraaijeveld
# @JMKraaijeveld
# kaidence.org
#############
import sys
from math import sqrt, log10

def is_palindrome(num):
    old = num
    new = 0
    while num > 0:
        digit = num % 10
        new = new * 10 + digit
        num = num / 10
    return new == old

# Open the files and read the arguments
input = open(sys.argv[1])
output = open(sys.argv[2], 'w')
numCases = int(input.readline())
current = 1

while current <= numCases:
    a, b = map(int, input.readline()[:-1].split())
    lower, upper = int(sqrt(a)), int(sqrt(b))
    count = 0
    i = lower
    while i <= upper+1:
        if i**2 >= a and i**2 <= b and is_palindrome(i) and is_palindrome(i**2):
           count += 1 
        i += 1
#    print "Case #{}: {}\n".format(current, count)
    output.write("Case #{}: {}\n".format(current, count))
    current += 1

