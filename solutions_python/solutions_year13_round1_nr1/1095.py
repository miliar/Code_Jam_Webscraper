import string
import math

num_cases = 0

def iterate_over_input(f_input_name, f_output_name):
    global num_cases
    f_input = open(f_input_name,'r')
    f_output = open(f_output_name,'w')
    num_cases = int(f_input.readline())
    for caseno,line in enumerate(f_input):
        result = process_case(line,f_input)
        write_output(caseno+1,result,f_output)
    f_input.close()
    f_output.close()

def write_output(caseno, result, f_output):
    f_output.write('Case #')
    f_output.write(str(caseno))
    f_output.write(': ')
    f_output.write(result)
    f_output.write('\n')

def process_case(line, f_input):
    parsed = [int(i) for i in line.split(' ')]
    r = parsed[0]
    t = parsed[1]
    a = 2
    b = 2*r +3
    c = 2*r +1 - t  
    delta = b**2 - 4*a*c
    s = math.floor(((-b + math.sqrt(delta))/(2*a)))
    tot1 = a*(s**2) + b*s + c
    if(tot1 > 0):
       return(str(s))
    else:
       return(str(s+1))
    return(str(s))

def solve():
    iterate_over_input('A-small-attempt1.in','A-small-attempt1.out')
    return 'DONE'

    
print(solve())
