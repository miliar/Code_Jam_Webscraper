##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

input = open('A-small-attempt0.in', 'r')
output = open('A-small.out', 'w')

##input = open('A-large.in', 'r')
##output = open('A-large.out', 'w')

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(g1, g2):
##    print g1
##    print g2
    answers = []
    for x in g2:
        if x in g1:
            answers.append(x)
    if len(answers) == 1:
        return str(answers[0])
    if len(answers) == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        a1 = read_int()
        for i in range(4):
            if i == a1 - 1:
                g1 = read_ints()
            else:
                dog = read_ints()
        a2 = read_int()
        for i in range(4):
            if i == a2 - 1:
                g2 = read_ints()
            else:
                dog = read_ints()
##        if case == 1:
        solution = solve(g1, g2)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
