import pprint
pp = pprint.PrettyPrinter(indent=4)

def ParseInput(filename):
    problems = []
    with open(filename, "r") as f:
        num_problems = int(f.readline())
        for i in range(num_problems):
            board = []
            for j in range(4):
                board.append(f.readline())
            problems.append(board)
            f.readline()
            
    return problems
        

def SolveProblem(problem):
    board = problem
    for i in range(4):
        current_winner = " "
        for j in range(4):
            cell = board[i][j]
            if cell == "T":
                continue
            if current_winner == " ":
                current_winner = cell
            if current_winner != cell:
                current_winner = "."
        if current_winner in ["X", "O"]:
            return current_winner + " won"
        
        
    for j in range(4):
        current_winner = " "
        for i in range(4):
            cell = board[i][j]
            if cell == "T":
                continue
            if current_winner == " ":
                current_winner = cell
            if current_winner != cell:
                current_winner = "."
        if current_winner in ["X", "O"]:
            return current_winner + " won"
        
    current_winner = " "
    for i in range(4):
        cell = board[i][i]
        if cell == "T":
            continue
        if current_winner == " ":
            current_winner = cell
        if current_winner != cell:
            current_winner = "."
    if current_winner in ["X", "O"]:
        return current_winner + " won"
    
    
    current_winner = " "
    for i in range(4):
        cell = board[i][3-i]
        if cell == "T":
            continue
        if current_winner == " ":
            current_winner = cell
        if current_winner != cell:
            current_winner = "."
    if current_winner in ["X", "O"]:
        return current_winner + " won"
    
    
    for i in range(4):
        for j in range(4):
            cell = board[i][j]
            if cell == ".":
                return "Game has not completed"
            
            
    return "Draw"
            
            
                
    

def SolveAndPrint(problems):
    current_problem = 1
    for problem in problems:
        answer = SolveProblem(problem)
        print ("Case #%d:" % current_problem), answer
        current_problem += 1
    
    
SolveAndPrint(ParseInput("A-large.in"))