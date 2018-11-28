#!/usr/bin/env python3

from ortools.linear_solver import pywraplp as lp
import sys

testcases = int(input())

for caso in range(1, testcases + 1):
    (n, m) = [int(x) for x in input().split(" ")]
    grid = [[0 for i in range(n)] for i in range(n)]
    for i in range(m):
        tmp = input().split()
        symbol = tmp[0]
        row = int(tmp[1]) - 1
        col = int(tmp[2]) - 1
        if symbol == "+":
            grid[row][col] = 1
        elif symbol == "x":
            grid[row][col] = 2
        elif symbol == "o":
            grid[row][col] = 3
    new_grid = []
    optimal_value = 0
    if n == 1:
        new_grid = [[3]]
        optimal_value = 2
    else:
        solver = lp.Solver("SolveIntegerProblem", lp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
        var = [[[solver.IntVar(0.0, 1.0, "x" + str(i) + "e" + str(j) + "e" + str(k)) for k in range(n)] for j in range(n)] for i in range(4)]
        # Valori delle singole celle
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 3:
                    constraint = solver.Constraint(1.0, 1.0)
                    constraint.SetCoefficient(var[3][row][col], 1)
                    constraint = solver.Constraint(0.0, 0.0)
                    constraint.SetCoefficient(var[0][row][col], 1)
                    constraint = solver.Constraint(0.0, 0.0)
                    constraint.SetCoefficient(var[1][row][col], 1)
                    constraint = solver.Constraint(0.0, 0.0)
                    constraint.SetCoefficient(var[2][row][col], 1)
                elif grid[row][col] == 2:
                    constraint = solver.Constraint(1.0, 1.0)
                    constraint.SetCoefficient(var[2][row][col], 1)
                    constraint.SetCoefficient(var[3][row][col], 1)
                    constraint = solver.Constraint(0.0, 0.0)
                    constraint.SetCoefficient(var[0][row][col], 1)
                    constraint = solver.Constraint(0.0, 0.0)
                    constraint.SetCoefficient(var[1][row][col], 1)
                elif grid[row][col] == 1:
                    constraint = solver.Constraint(1.0, 1.0)
                    constraint.SetCoefficient(var[1][row][col], 1)
                    constraint.SetCoefficient(var[3][row][col], 1)
                    constraint = solver.Constraint(0.0, 0.0)
                    constraint.SetCoefficient(var[0][row][col], 1)
                    constraint = solver.Constraint(0.0, 0.0)
                    constraint.SetCoefficient(var[2][row][col], 1)
                elif grid[row][col] == 0:
                    constraint = solver.Constraint(1.0, 1.0)
                    constraint.SetCoefficient(var[0][row][col], 1)
                    constraint.SetCoefficient(var[1][row][col], 1)
                    constraint.SetCoefficient(var[2][row][col], 1)
                    constraint.SetCoefficient(var[3][row][col], 1)
        # Controlli righe
        for row in range(n):
            constraint = solver.Constraint(-solver.infinity(), 1.0)
            for col in range(n):
                constraint.SetCoefficient(var[2][row][col], 1)
                constraint.SetCoefficient(var[3][row][col], 1)
        # Controlli colonne
        for col in range(n):
            constraint = solver.Constraint(-solver.infinity(), 1.0)
            for row in range(n):
                constraint.SetCoefficient(var[2][row][col], 1)
                constraint.SetCoefficient(var[3][row][col], 1)
        # Diagonali / riga sopra
        for col in range(1, n):
            r = 0
            c = col
            constraint = solver.Constraint(-solver.infinity(), 1.0)
            while c >= 0:
                constraint.SetCoefficient(var[1][r][c], 1)
                constraint.SetCoefficient(var[3][r][c], 1)
                r += 1
                c -= 1
        # Diagonali \ riga sopra
        for col in range(n - 1):
            r = 0
            c = col
            constraint = solver.Constraint(-solver.infinity(), 1.0)
            while c < n:
                constraint.SetCoefficient(var[1][r][c], 1)
                constraint.SetCoefficient(var[3][r][c], 1)
                r += 1
                c += 1
        # Diagonali / riga sotto
        for col in range(1, n - 1):
            r = n - 1
            c = col
            constraint = solver.Constraint(-solver.infinity(), 1.0)
            while c < n:
                constraint.SetCoefficient(var[1][r][c], 1)
                constraint.SetCoefficient(var[3][r][c], 1)
                r -= 1
                c += 1
        # Diagonali \ riga sotto
        for col in range(1, n - 1):
            r = n - 1
            c = col
            constraint = solver.Constraint(-solver.infinity(), 1.0)
            while c >= 0:
                constraint.SetCoefficient(var[1][r][c], 1)
                constraint.SetCoefficient(var[3][r][c], 1)
                r -= 1
                c -= 1
        objective = solver.Objective()
        for i in range(1, 4):
            for row in range(n):
                for col in range(n):
                    if i == 1 or i == 2:
                        objective.SetCoefficient(var[i][row][col], 1)
                    elif i == 3:
                        objective.SetCoefficient(var[i][row][col], 2)
        objective.SetMaximization()
        result_status = solver.Solve()
        assert result_status == lp.Solver.OPTIMAL
        assert solver.VerifySolution(1e-7, True)
        for row in range(n):
            l = []
            for col in range(n):
                if var[0][row][col].solution_value() == 1.0:
                    l.append(0)
                elif var[1][row][col].solution_value() == 1.0:
                    l.append(1)
                elif var[2][row][col].solution_value() == 1.0:
                    l.append(2)
                elif var[3][row][col].solution_value() == 1.0:
                    l.append(3)
                else:
                    assert 0
            new_grid.append(l)
        optimal_value = int(round(solver.Objective().Value()))
    diffs = []
    for row in range(n):
        for col in range(n):
            if grid[row][col] != new_grid[row][col]:
                if new_grid[row][col] == 1:
                    diffs.append(('+', row + 1, col + 1))
                elif new_grid[row][col] == 2:
                    diffs.append(('x', row + 1, col + 1))
                elif new_grid[row][col] == 3:
                    diffs.append(('o', row + 1, col + 1))
                else:
                    assert 0
    print("Case #", caso, sep='', file=sys.stderr, flush=True)
    print("Case #", caso, ": ", optimal_value, " ", len(diffs), sep='')
    for diff in diffs:
        print(diff[0], diff[1], diff[2])
