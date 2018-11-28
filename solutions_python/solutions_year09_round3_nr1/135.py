#import psyco
import string


order = [1,0,2,3,4,5,6,7,8,9]
order = [str(i) for i in order]
order = order + list(string.lowercase)


def solve(alien_number):
    mapping = {}
    
    regular_number = []
    
    i = 0
    
    for digit in alien_number:
        if digit in mapping:
            regular_number.append( mapping[digit] )
        else:
            regular_number.append ( order[i] )
            mapping[digit] = order[i]
            i+= 1
            
    if i < 2:
        i = 2
    return int(''.join(regular_number), i)
    
def main():
    number_of_cases = int(raw_input())
    for case_number in range(1, number_of_cases+1):
        alien_number = raw_input()
        
        print 'Case #%d: %d' % (case_number, solve(alien_number))
        
main()

#print solve('11001001')
#print solve('cats')
#print solve('zig')