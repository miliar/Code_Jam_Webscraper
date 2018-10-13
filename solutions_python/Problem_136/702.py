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

def solve(data):
    C = data[0]
    F = data[1]
    X = data[2]
    m = 2.0
    total = 0
    while X / m > C / m + X / (m + F):
        total += C / m
##        print total
        m += F
    total += X / m
    return total

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        data = read_floats()
##        if case == 4:
        solution = solve(data)
        solution_string = "Case #%d: %0.7f" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
