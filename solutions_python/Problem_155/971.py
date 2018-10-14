class Problem:
    def __init__(self) :
        self.max = 0
        self.members = []

def readProblem(input):
    problem = Problem()
    data = input.readline().split()
    problem.max = int(data[0])
    for i in range(len(data[1])) :
        problem.members.append(int(data[1][i]))
    return problem

def solveProblem(problem):
    to_invite = 0
    standing = 0
    for i in range(len(problem.members)) :
        if (standing >= i) :
            standing  = standing + problem.members[i]
        elif problem.members[i] > 0 :
            to_invite = to_invite + (i - standing)
            standing = i + problem.members[i]   
    
    return to_invite

input = open('input.in')
output = open('output.out', 'w')

cases = int(input.readline())
for i in range(cases):
    problem = readProblem(input)
    answer = solveProblem(problem)
	
    output.write("Case #" + str(i+1) + ": " + str(answer) + "\n")

