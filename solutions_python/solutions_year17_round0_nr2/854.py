##input = open('B-sample-input.txt', 'r')
##output = open('B-sample-output.txt', 'w')

##input = open('B-small-attempt0.in', 'r')
##output = open('B-small.out', 'w')

input = open('B-large.in', 'r')
output = open('B-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(T):
    s = [int(x) for x in str(T)]
    if len(s) == 1:
        return str(T)
    for i in range(len(s) - 2, -1, -1):
##        print s
        if s[i] == - 1:
            s[i] = 9
            s[i - 1] -= 1
        if s[i] > s[i + 1]:
            for j in range(i + 1, len(s), 1):
                s[j] = 9
            if s[i] == 0:
                s[i] = 9
                s[i - 1] -= 1
            else:
                s[i] -= 1
    first_zero = True
    while first_zero:
        if s[0] == 0:
            s = s[1:]
        else:
            first_zero = False
    return "".join([str(x) for x in s])

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        T = read_int()
##        if case == 4:        
        solution = solve(T)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
