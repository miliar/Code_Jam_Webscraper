import time
import logging
from ortools.linear_solver import pywraplp


def solve_fashion(n, board, m):
    solver = pywraplp.Solver('SolveQueen',
                             pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    circles = [[] for _ in range(n)]
    crosses = [[] for _ in range(n)]
    plusses = [[] for _ in range(n)]

    preplaced_constraints = [None] * m
    pc_idx = 0
    objective = solver.Objective()
    for i in range(n):
        circles[i] = [None for _ in range(n)]
        crosses[i] = [None for _ in range(n)]
        plusses[i] = [None for _ in range(n)]
        for j in range(n):
            circle_value = 0
            if board[i][j] == 'o':
                circle_value = 1
            circles[i][j] = solver.IntVar(circle_value, 1,
                                          "O:r" + str(i) + "c" + str(j))
            crosses[i][j] = solver.IntVar(0, 1, "X:r" + str(i) + "c" + str(j))
            plusses[i][j] = solver.IntVar(0, 1, "+:r" + str(i) + "c" + str(j))
            if board[i][j] == 'x':
                preplaced_constraints[pc_idx] = solver.Constraint(1, 1)
                preplaced_constraints[pc_idx].SetCoefficient(circles[i][j], 1)
                preplaced_constraints[pc_idx].SetCoefficient(crosses[i][j], 1)
            if board[i][j] == '+':
                preplaced_constraints[pc_idx] = solver.Constraint(1, 1)
                preplaced_constraints[pc_idx].SetCoefficient(circles[i][j], 1)
                preplaced_constraints[pc_idx].SetCoefficient(plusses[i][j], 1)


            objective.SetCoefficient(circles[i][j], 2.001)
            objective.SetCoefficient(crosses[i][j], 1)
            objective.SetCoefficient(plusses[i][j], 1)
    objective.SetMaximization()

    row_constraints = [None] * n
    for i in range(0, n):
        row_constraints[i] = solver.Constraint(1, 1)
        for j in range(0, n):
            row_constraints[i].SetCoefficient(circles[i][j], 1)
            row_constraints[i].SetCoefficient(crosses[i][j], 1)

    col_constraints = [None] * n
    for i in range(0, n):
        col_constraints[i] = solver.Constraint(1, 1)
        for j in range(0, n):
            col_constraints[i].SetCoefficient(circles[j][i], 1)
            col_constraints[i].SetCoefficient(crosses[j][i], 1)

    inc_diag_constraints = {}
    for i in range(0, n):
        for j in range(0, n):
            if i + j not in inc_diag_constraints:
                inc_diag_constraints[i + j] = solver.Constraint(0, 1)
            inc_diag_constraints[i + j].SetCoefficient(circles[i][j], 1)
            inc_diag_constraints[i + j].SetCoefficient(plusses[i][j], 1)

    dec_diag_constraints = {}
    for i in range(0, n):
        for j in range(0, n):
            if i - j not in dec_diag_constraints:
                dec_diag_constraints[i - j] = solver.Constraint(0, 1)
            dec_diag_constraints[i - j].SetCoefficient(circles[i][j], 1)
            dec_diag_constraints[i - j].SetCoefficient(plusses[i][j], 1)

    # Solve!
    status = solver.Solve()
    if status == solver.OPTIMAL:
        style = 0

        changed = []

        for i in range(n):
            for j in range(n):
                if circles[i][j].solution_value() == 1:
                    if board[i][j] != 'o':
                        changed.append(('o', i, j))
                    style += 2
                    # print('O ', end='')
                elif crosses[i][j].solution_value() == 1:
                    if board[i][j] != 'x':
                        changed.append(('x', i, j))
                    style += 1
                    # print('X ', end='')
                elif plusses[i][j].solution_value() == 1:
                    if board[i][j] != '+':
                        changed.append(('+', i, j))
                    style += 1
                    # print('+ ', end='')
                else:
                    pass
                    # print('_ ', end='')
            # print()
        return style, changed
    else:  # No optimal solution was found.
        if status == solver.FEASIBLE:
            print('A potentially suboptimal solution was found.')
        else:
            print('The solver could not solve the problem.')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='logs/log-{}.log'.format(time.time()),
                        filemode='w')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    total_elapsed_time = 0

    t = int(input())
    for test in range(1, t + 1):
        logging.info('Test #{}/{} started'.format(test, t))
        start_time = time.time()
        n, m = [int(s) for s in input().split(" ")]

        board = [[] for x in range(n)]
        for x in range(n):
            board[x] = [None for _ in range(n)]

        for j in range(m):
            type, i, j = [s for s in input().split(" ")]
            i = int(i) - 1
            j = int(j) - 1
            board[i][j] = type

        style, changed = solve_fashion(n, board, m)

        print("Case #{}: {} {}".format(test, style, len(changed)))
        for c in changed:
            print("{} {} {}".format(c[0], c[1] + 1, c[2] + 1))

        elapsed = time.time() - start_time
        total_elapsed_time += elapsed
        logging.info('Test #{}/{} ended. Time: {:.2f}'.format(test, t, elapsed))
        logging.info('Elapsed time: {:.2f}, Expected Total: {:.2f}'.format(
            total_elapsed_time,
            total_elapsed_time + (total_elapsed_time / test) * (t - test))
        )
