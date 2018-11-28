in_put = open("input.in", 'r')
output = open("output.out", 'w')

ABSOLUTE_MAX_UPPER = 10100

test_count = int(in_put.next())
limits = []
max_upper_limit = 0

palindromes = []
squares = [] # squares of palindromes, i.e. FnS numbers

for test in range(1, test_count + 1):
    current_limits = in_put.next().split()
    lower = int(current_limits[0])
    upper = int(current_limits[1])
    limits.append([lower, upper])
    
    if upper > max_upper_limit:
        max_upper_limit = upper
     
def is_palindrome(string):
    length = len(string)
    for i in range(0, length / 2):
        if string[i] != string[length - i - 1]:
            return False
        
    return True
        
def calculate_FnS_up_to(limit):
    for i in range(0, limit + 1): # up to sqrt(limit), should suffice
        if is_palindrome(str(i)):
            square = i**2
            palindromes.append(i)
            squares.append(square)

# pre generate FnSs smaller than maximum limit for the whole input data
calculate_FnS_up_to(max_upper_limit)

for test in range(1, test_count + 1):
    if test > 1:
        output.write("\n")
    
    FnS_count = 0
    current_limits = limits[test - 1]
    for FnS in squares:
        if FnS >= current_limits[0] and FnS <= current_limits[1] and FnS in palindromes:
            FnS_count += 1
            
    output.write("Case #" + str(test) + ": " + str(FnS_count))