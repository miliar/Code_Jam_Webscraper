##input = open('C-sample-input.txt', 'r')
##output = open('C-sample-output.txt', 'w')
#input = open('/Users/pruthvikarreddy/Downloads/test.in', 'r')
import math
input = open('A-small-attempt0 (2).in', 'r')
output = open('A-small.out', 'w')

##input = open('C-large.in', 'r')
##output = open('C-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]
    
def read_frac():
    return [int(x) for x in input.readline().split('/')]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]
    
def read_floats():
    return [float(x) for x in input.readline().split()]
    
def read_strs():
    return [x for x in input.readline().split()]

def read_str():
    return input.readline().strip()
    
def read_floats():
    return input.readline().split()

def solve(N, perm):
    return 'ans'

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        t,b=read_frac()
        lt,lb=math.log(t,2),math.log(b,2)
        logs=lb-lt
        if logs==int(logs) or lb==int(lb):
            solution=int(math.ceil(logs))
        else:
            solution='impossible'
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        
if __name__=='__main__':
    main()
    input.close()
    output.close()
    
