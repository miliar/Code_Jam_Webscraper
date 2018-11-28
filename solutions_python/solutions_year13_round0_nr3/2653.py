import sys
import math
import cjinput
    
def main():
    lines = [line.strip() for line in sys.stdin]
    test_cases = cjinput.read_input(lines, cjinput.simple_line_list_case)
    for c,case in enumerate(test_cases):
        count = 0
        start = int(case[0])
        end = int(case[1])
        for i in range(start, end + 1):
            count += 1 if check_if_fair_and_square(i) else 0
        print "Case #%i: %i" % (c + 1, count)

def check_if_palindrome(s):
    is_palindrome = True
    for i in range(len(s) / 2):
        if s[i] != s[-i-1]:
            is_palindrome = False
    return is_palindrome    

sq_cache = {}
def calc_squareroot(num):
    if (not num in sq_cache):
        sq_cache[num] = math.sqrt(num)
    return sq_cache[num]
        
def check_if_square(num):
    sq = calc_squareroot(num)
    return sq - math.floor(sq) == 0.0

def check_if_fair_and_square(num):
    if not check_if_palindrome(str(num)):
        return False
    if not check_if_square(num):
        return False
    sq = int(calc_squareroot(num))
    if not check_if_palindrome(str(sq)):
        return False
    return True
    
if __name__ == '__main__':
    main()