from math import ceil, floor, sqrt

f = open('C-small-attempt0.in','r')
input_file = [x.strip() for x in f.readlines()]
f.close()

n_cases = int(input_file.pop(0))
input_cases = []

while len(input_file)>0:
    A,B = [int(x) for x in input_file[0].split()]
    input_file = input_file[1:]
    input_cases.append((A,B))
    



def check_palindrome(query_number):
    number_string = str(query_number)
    for i in range(len(number_string)//2):
        if number_string[i] != number_string[-1-i]:
            return False
    return True
    

def solve_problem(case):
    A,B = case
    #round up sqrt of lower bound
    #round down sqrt of upper bound
    lower = int(ceil(sqrt(A)))
    upper = int(floor(sqrt(B)))
    
    count = 0
    for x in range(lower,upper+1):
        if check_palindrome(x):
            if check_palindrome(x**2):
                count += 1
    return  str(count)

f = open('C_small_solution.txt','w')
for i,x in enumerate(input_cases):
    f.write('Case #' + str(i+1) + ': ' + solve_problem(x) + '\n')
f.close()