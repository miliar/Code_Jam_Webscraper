from helpers.logs import Logger
from ortools.linear_solver import pywraplp

colors = ['R', 'O', 'Y', 'G', 'B', 'V']

def input_function():
    data = {}
    amounts = [int(s) for s in input().split(' ')]
    N = amounts.pop(0)
    data['amounts'] = {colors[i]: amounts[i] for i in range(len(colors))}
    data['N'] = N
    return data


def solution_function(test_num, test_input, general_input):
    data = test_input[test_num]

    N = data['N']
    amounts = data['amounts']

    solver = pywraplp.Solver('SolveQueen',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    placements = {c: [None for _ in range(N)] for c in colors}

    objective = solver.Objective()

    # init variables and objective
    for i in range(N):
        for color in colors:
            placements[color][i] = solver.IntVar(0, 1, color + ":i" + str(i))
            objective.SetCoefficient(placements[color][i], 1)

    # one at any place constraint
    for i in range(N):
        constraint = solver.Constraint(1, 1)
        for color in colors:
            constraint.SetCoefficient(placements[color][i], 1)

    # input constraints
    for color in colors:
        constraint = solver.Constraint(amounts[color], amounts[color])
        for i in range(N):
            constraint.SetCoefficient(placements[color][i], 1)

    # adjacent similar constraint
    for i in range(N):
        # R
        constraint = solver.Constraint(0, 1)
        for color in ['R', 'O', 'V']:
            constraint.SetCoefficient(placements[color][i], 1)
            constraint.SetCoefficient(placements[color][(i + 1) % N], 1)
        # B
        constraint = solver.Constraint(0, 1)
        for color in ['B', 'G', 'V']:
            constraint.SetCoefficient(placements[color][i], 1)
            constraint.SetCoefficient(placements[color][(i + 1) % N], 1)
        # Y
        constraint = solver.Constraint(0, 1)
        for color in ['Y', 'O', 'G']:
            constraint.SetCoefficient(placements[color][i], 1)
            constraint.SetCoefficient(placements[color][(i + 1) % N], 1)

    objective.SetMaximization()

    # Solve!
    status = solver.Solve()
    if status == solver.OPTIMAL:
        answer = ''
        for i in range(N):
            for color in colors:
                if placements[color][i].solution_value() == 1:
                    answer += color
    else:  # No optimal solution was found.
        answer = 'IMPOSSIBLE'

    print('Case #{}: {}'.format(test_num + 1, answer))


logger = Logger(solution_function, input_function)
logger.start()
