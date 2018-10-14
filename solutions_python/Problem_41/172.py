#import psyco

def has_all_digits(number_as_str, expected_digit_count):
    digit_count = {}
    for i in [1,2,3,4,5,6,7,8,9]:
        digit_count[str(i)] = 0
    
    for digit in number_as_str:
        if digit != '0':
            digit_count[digit] += 1
        
    good = expected_digit_count == digit_count
    
    return good
    

def next_number(number, expected_digit_count):
    while True:
        number += 1
        if has_all_digits( str(number), expected_digit_count ):
            break
        
    return number

def solve(number_as_str):
    digit_count = {}
    for i in [1,2,3,4,5,6,7,8,9]:
        digit_count[str(i)] = 0
    for digit in number_as_str:
        if digit != '0':
            digit_count[digit] += 1
        
    number = int(number_as_str)
    
    next = next_number(number, digit_count)
    
    return next


def main():
    number_of_cases = int(raw_input())
    
    for case_number in range(1, number_of_cases+1):
        number_as_str = raw_input()
        print 'Case #%d: %d' % (case_number, solve(number_as_str))
        
main()

#print solve(str(13256040))
#print solve(str(1051))
#print solve(str(6233))