import sys

def solvable(m):
    chars = set(c for row in m for c in row if c != '?')
    if len(chars) == 0:
        return False
    return True

def solve(m):
    chars = set(c for row in m for c in row if c != '?')
    if len(chars) == 0:
        raise RuntimeError("tried to solve empty case")
    elif len(chars) == 1:
        [char] = chars
        return [[char for _ in row] for row in m]

    for i in range(1, len(m)):
        upper = m[:i]
        lower = m[i:]
        if solvable(upper) and solvable(lower):
            return solve(upper) + solve(lower)

    for j in range(1, len(m[0])):
        left = [row[:j] for row in m]
        right = [row[j:] for row in m]
        if solvable(left) and solvable(right):
            left_sol = solve(left)
            right_sol = solve(right)
            return [left_row + right_row for left_row, right_row in zip(left_sol, right_sol)]

    raise RuntimeError("for some reason this case seems impossible: {}".format(m))

def main():
    case_count = int(next(sys.stdin))
    for case_number in range(1, case_count + 1):
        r, c = map(int, next(sys.stdin).split())
        m = []
        for i in range(r):
            m.append(list(next(sys.stdin).strip()))

        solution = solve(m)
        print(f"Case #{case_number}:")
        for row in solution:
            print("".join(row))

if __name__ == "__main__":
    main()
