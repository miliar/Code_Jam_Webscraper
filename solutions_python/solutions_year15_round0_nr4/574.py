import math 

class Problem:
    def __init__(self) :
        self.data = {"X": 0, "R": 0, "C": 0}
        self.X = 0
        self.X = 0

def readProblem(input):
    problem = Problem()
    line = input.readline().split()
    problem.data["X"] = int(line[0]);
    problem.data["R"] = int(line[1]);
    problem.data["C"] = int(line[2]);    
    return problem

def solveProblem(problem):
    answer = "There is no solution."
    
    if ((problem.data["R"] * problem.data["C"]) % problem.data["X"] != 0) :
        answer = "RICHARD"
    elif (int(math.ceil(problem.data["X"]/2.0)) > min(problem.data['R'], problem.data['C'])) :
        answer = "RICHARD"
    elif ((problem.data['X'] in {4,6})  and \
          (min(problem.data['R'], problem.data['C']) <= problem.data["X"]/2)) :
        # if the minimum dimension isn't wider than half the length
        # you can force the user to create a region that isn't even in number
        # and this can never be filled
        answer = "RICHARD"
    elif ((problem.data['X'] == 5) and \
          (min(problem.data['R'], problem.data['C']) == 2) and \
          (problem.data["R"] * problem.data["C"] < 3 * problem.data["X"])) :
        # as long as there is enough space above and below you can make this work
        answer = "RICHARD"
    elif ((problem.data['X'] == 5) and \
          (min(problem.data['R'], problem.data['C']) == 3) and \
          (min(problem.data['R'], problem.data['C']) <= int(math.ceil(problem.data["X"]/2.0)))) :
        # if the minimum dimension isn't wider than the ceiling of half the length
        # you can force the user to create a region that isn't odd in number
        # and this can never be filled
        answer = "RICHARD"
    elif (problem.data['X'] > 6) :
        # X-ominoes of greater than 6 cells all have one shape that has a hole in it
        # if this piece is picked then the other player can never win
        answer = "RICHARD"
    else :
        answer = "GABRIEL"
        
    
    return answer #+ "  (" + str(problem.data["X"]) + ", " + str(problem.data["R"]) + ", " + str(problem.data["C"]) + ")"



input = open('input.in')
output = open('output.out', 'w')

cases = int(input.readline())
for i in range(cases):
    problem = readProblem(input)
    answer = solveProblem(problem)
	
    output.write("Case #" + str(i+1) + ": " + str(answer) + "\n")

