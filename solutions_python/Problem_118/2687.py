import math
import sys

def is_palindrome(x):
    x = str(int(x))
    return x == x[::-1]

def get_numbers(a, b):
    total = 0
    start = int(math.ceil(math.sqrt(float(a))))
    end = int(math.floor(math.sqrt(float(b))))
    
    for x in range(start, end+1):
        if is_palindrome(x) and is_palindrome(x*x):
            total += 1
            
    return total

if __name__ == "__main__":
    sys.stdin.next()
    case_counter = 0

    for line in sys.stdin:
        case_counter += 1
        inputs = line.split(" ")
        print "Case #{}: {}".format(case_counter, 
            get_numbers(inputs[0], inputs[1]))
