# python 3

from math import sqrt

def read_input():
    num_cases = int(input())
    return [[int(x) for x in input().split()] for case in range(num_cases)]
    

def is_palindrome(n):
    s = str(n)
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    return True
    
    
def is_fairsquare(n):
    root = sqrt(n)
    
    if not is_palindrome(n):
        return False
    if root % 1 != 0:
        return False
    root = int(root)
    return is_palindrome(root)
        
    
def count_fairsquare(lower_inc, upper_inc):
    return len([n for n in range(lower_inc, upper_inc+1) if is_fairsquare(n)])
    
    
if __name__ == '__main__':
    cases = read_input()
    for i in range(len(cases)):
        lower, upper = cases[i]
        case_num = i + 1
        print('Case #{0}: {1}'.format(case_num, count_fairsquare(lower, upper)))