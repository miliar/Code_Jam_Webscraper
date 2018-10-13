import pprint
pp = pprint.PrettyPrinter(indent=4)


def ParseInput(filename):
    problems = []
    with open(filename, "r") as f:
        num_problems = int(f.readline())
        for i in range(num_problems):
            current_problem = []
            num_vines = int(f.readline())
            for j in range(num_vines):
                vine = [int(x) for x in f.readline().split(" ")]
                current_problem.append(vine)
            current_problem.append(int(f.readline()))
            problems.append(current_problem)
        
    return problems
        

def SolveProblem(problem):
    love_distance = problem[-1]
    vines = problem[:-1]
    
    vines = [[0,0]] + vines
    
    memo_table = []
    for i in range(len(vines)):
        memo_line = []
        for j in range(len(vines)):
            memo_line.append(-1)
        memo_table.append(memo_line)
        
    def can_reach_end(vine1, vine2):
        if memo_table[vine1][vine2] != -1:
            return memo_table[vine1][vine2]
        
        vines_distance = vines[vine2][0] - vines[vine1][0]
        travelable_distance = min(vines_distance, vines[vine2][1])
        furthest_reachable = travelable_distance + vines[vine2][0]
        if furthest_reachable >= love_distance:
            return 1
        
        for next_vine in range(vine2 + 1,len(vines)):
            if vines[next_vine][0] > furthest_reachable:
                memo_table[vine1][vine2] = 0
                return 0
            reachable = can_reach_end(vine2, next_vine)
            if reachable == 1:
                return 1
            
        memo_table[vine1][vine2] = 0
        return 0
    
    answer = can_reach_end(0,1)
    if answer == 1:
        return "YES"
    else:
        return "NO"
    

def SolveAndPrint(problems):
    current_problem = 1
    for problem in problems:
        answer = SolveProblem(problem)
        print ("Case #%d:" % current_problem), answer
        current_problem += 1
    
    
SolveAndPrint(ParseInput("A-small-attempt0.in"))