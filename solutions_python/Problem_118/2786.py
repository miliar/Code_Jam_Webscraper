from math import sqrt, floor, ceil

def is_pal(n):
    """
    True if int_in_question is an integer that is a
    palindrome when written in base 10.
    """
    # Change the number into a string and then a list.
    as_list_of_chars = list(str(n))
    # Copy the list and reverse it.
    reversed_list_of_chars = list(as_list_of_chars)
    reversed_list_of_chars.reverse()
    # True if the list of chars is palindromic.
    return as_list_of_chars == reversed_list_of_chars

def solve(a, b):
    result_list = []
    #print a, b
    sqrt_a = int(ceil(sqrt(a))); sqrt_b = int(floor(sqrt(b)))
    #print sq_a, sq_b, range(sq_a, sq_b+1)

    for sqrt_n in filter(is_pal, range(sqrt_a, sqrt_b+1)):
        n = sqrt_n**2
        if is_pal(n):
            result_list.append(n)
    #print result_list
    return len(result_list)

#input, solve and output:
                        
input = open('C-small-attempt0.in', 'r')
output = open('C-small-attempt0.out', 'w')


num_cases = int(input.readline())
for case in range(1, num_cases+1):
        a, b = map(int, input.readline().strip().split())

        result = solve(a, b)

        #print case, result
        #print 
        output.write('Case #%s: %s\n' %(case, result))

input.close()
output.close()

