from collections import defaultdict


def compute(grid, R, C):


    d = defaultdict(int)
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '.':
                if grid[i][j] == '<':
                    d[(i,j)] += 1
                break


    for i in range(R):
        for j in reversed(range(C)):
            if grid[i][j] != '.':
                if grid[i][j] == '>':
                    d[(i,j)] += 1
                break

    for j in range(C):
        for i in reversed(range(R)):
            if grid[i][j] != '.':
                if grid[i][j] == 'v':
                    d[(i,j)] += 1
                break



    for j in range(C):
        for i in range(R):
            if grid[i][j] != '.':
                if grid[i][j] == '^':
                    d[(i,j)] += 1
                break


    t = defaultdict(int)
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '.':
                t[(i,j)] += 1
                break


    for i in range(R):
        for j in reversed(range(C)):
            if grid[i][j] != '.':
                t[(i,j)] += 1
                break

    for j in range(C):
        for i in reversed(range(R)):
            if grid[i][j] != '.':
                t[(i,j)] += 1
                break


    for j in range(C):
        for i in range(R):
            if grid[i][j] != '.':
                t[(i,j)] += 1
                break



    for key, value in t.items():
        if value == 4:
            return "IMPOSSIBLE"

    return len(d)


def read_number(f):
    return int(f.readline().strip())

def read_numbers(f):
    return map(int, f.readline().strip().split())

def main():
    with open('A-large.in', 'r') as f:
        test_cases = read_number(f)

        for test_case in range(test_cases):
            R,C = read_numbers(f)
            grid = []
            for i in range(R):
                grid.append(f.readline().strip())
            result = compute(grid, R, C)
            print('Case #{}: {}'.format(test_case + 1, result))

if __name__ == '__main__':
    main()