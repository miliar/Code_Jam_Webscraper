import sys
import math

def is_palindrome(s):
    for i in range(len(s)/2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True
    
def is_square_of_palin(x):
    root = math.sqrt(x)
    if (root % 1 != 0):
        return False
    return is_palindrome(str(int(root)))
    
def main():
    f = open(sys.argv[1], 'r')

    f.readline()
    line = f.readline()
    case = 1
    while line:
        count = 0
        bounds = line.split(' ')
        a = int(bounds[0])
        b = int(bounds[1])

        for i in range(a, b+1):
            if is_palindrome(str(i)) and is_square_of_palin(i):
                count += 1
        print 'Case #' + str(case) + ': ' + str(count)
        case += 1
        line = f.readline()

if __name__ == "__main__":
    main()