class Problem:
    def __init__(self) :
        self.data = []

def readProblem(input):
    problem = Problem()
    count = int(input.readline())
    line = input.readline().split()
    for i in range(len(line)) :
        problem.data.append(int(line[i]))
    return problem

def solveProblem(problem):
    answer = "There is no solution."
	
    minimum = 0
    maximum = 0
    rate = 0
    previous = problem.data[0]

    for i in range(1, len(problem.data)) :
        value = problem.data[i]
        if (previous > value) :
            minimum += (previous - value)
        rate = max(rate, (previous - value))
        previous = value
        
    for i in range(0, len(problem.data)-1) :    
        maximum += min(rate, problem.data[i])
			
    return str(minimum) + " " + str(maximum)



input = open('input.in')
output = open('output.out', 'w')

cases = int(input.readline())
for i in range(cases):
    problem = readProblem(input)
    print problem.data
    answer = solveProblem(problem)
    print answer
	
    output.write("Case #" + str(i+1) + ": " + str(answer) + "\n")

