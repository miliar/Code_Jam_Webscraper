import numpy as np

def parse(filepath):
    f = open(filepath)
    cases = []
    test_case_nb = int(f.readline())
    for case_idx in range(test_case_nb):
        grids = []
        for grid_idx in range(2):
            answer = int(f.readline())
            grid = np.zeros((4,4))
            for row_idx in range(4):
                grid[row_idx] = f.readline().split()
            grid = grid.astype('int')
            grids.append((answer, grid))
        cases.append(grids)
    return cases

def solve(cases):
    solutions = []
    for case_idx in range(len(cases)):
        grids = cases[case_idx]
        solution = None
        for grid_idx, grid in enumerate(grids):
            row_idx = grid[0]-1
            if grid_idx == 0:
                solution = set(grid[1][row_idx].tolist())
            else:
                solution = solution.intersection(grid[1][row_idx])
        solutions.append(solution)
    return solutions

def write_results(solutions, output_filepath):
    f = open(output_filepath, 'w')
    lines = []
    for solution_idx, solution in enumerate(solutions):
        if len(solution) == 1:
            result = str(solution.pop())
        elif len(solution) > 1:
            result = "Bad magician!"
        elif len(solution) == 0:
            result = "Volunteer cheated!"
        lines.append("Case #%s: %s"%(solution_idx+1, result))
    f.write("\n".join(lines))


if __name__ == '__main__':
    import sys
    cases = parse(sys.argv[1])
    solutions = solve(cases)
    write_results(solutions, sys.argv[2])





