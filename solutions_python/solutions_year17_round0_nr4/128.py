import pulp
import multiprocessing


def answer(n, models):
    prob = pulp.LpProblem(sense=pulp.LpMaximize)
    p = [[pulp.LpVariable('+_{}_{}'.format(row, col), lowBound=0, upBound=1) for col in range(n)] for row in range(n)]
    c = [[pulp.LpVariable('x_{}_{}'.format(row, col), lowBound=0, upBound=1) for col in range(n)] for row in range(n)]
    o = [[pulp.LpVariable('o_{}_{}'.format(row, col), lowBound=0, upBound=1) for col in range(n)] for row in range(n)]

    stage = [['.' for col in range(n)] for row in range(n)]
    for model_char, row_p, col_p in models:
        row, col = row_p - 1, col_p - 1
        stage[row][col] = model_char
        if model_char == '+':
            p[row][col].bounds(0, 1)
            c[row][col].bounds(0, 0)
            o[row][col].bounds(0, 1)
            prob += 1 * p[row][col] + 1 * o[row][col] == 1
        elif model_char == 'x':
            p[row][col].bounds(0, 0)
            c[row][col].bounds(0, 1)
            o[row][col].bounds(0, 1)
            prob += 1 * c[row][col] + 1 * o[row][col] == 1
        else:
            p[row][col].bounds(0, 0)
            c[row][col].bounds(0, 0)
            o[row][col].bounds(1, 1)

    for diagonal_plus in range(2 * n - 1):
        constraint = []
        for row in range(max(0, diagonal_plus - n + 1), min(n, diagonal_plus + 1)):
            constraint.append((p[row][diagonal_plus - row], 1))
            constraint.append((o[row][diagonal_plus - row], 1))
        prob += pulp.LpAffineExpression(constraint) <= 1

    for diagonal_minus in range(-n + 1, n):
        constraint = []
        for row in range(max(0, -diagonal_minus), min(n, n - diagonal_minus)):
            constraint.append((p[row][diagonal_minus + row], 1))
            constraint.append((o[row][diagonal_minus + row], 1))
        prob += pulp.LpAffineExpression(constraint) <= 1

    for row in range(n):
        constraint = []
        for col in range(n):
            constraint.append((c[row][col], 1))
            constraint.append((o[row][col], 1))
        prob += pulp.LpAffineExpression(constraint) <= 1

    for col in range(n):
        constraint = []
        for row in range(n):
            constraint.append((c[row][col], 1))
            constraint.append((o[row][col], 1))
        prob += pulp.LpAffineExpression(constraint) <= 1

    for row in range(n):
        for col in range(n):
            prob += 1 * p[row][col] + 1 * c[row][col] + 1 * o[row][col] <= 1

    target = []
    for row in range(n):
        for col in range(n):
            target.append((p[row][col], 1))
            target.append((c[row][col], 1))
            target.append((o[row][col], 2))
    target_expr = pulp.LpAffineExpression(target)
    prob += target_expr

    lifted = True
    epsilon = 1e-15

    while lifted:
        prob.solve()

        lifted = False
        for var in (p, c, o):
            for row in range(n):
                for col in range(n):
                    if not lifted and epsilon < pulp.value(var[row][col]) <= 0.5:
                        lifted = True
                        var[row][col].bounds(0, 0)

        # print([[pulp.value(p[row][col]) for col in range(n)] for row in range(n)])
        # print([[pulp.value(c[row][col]) for col in range(n)] for row in range(n)])
        # print([[pulp.value(o[row][col]) for col in range(n)] for row in range(n)])
        # print(pulp.value(target_expr))

    changes = []
    for model_char, var in (('+', p), ('x', c), ('o', o)):
        for row in range(n):
            for col in range(n):
                if pulp.value(var[row][col]) >= 1 - epsilon and model_char != stage[row][col]:
                    changes.append((model_char, row + 1, col + 1))

    result = int(round(pulp.value(target_expr)))
    return result, changes


def main():
    cases = []

    t = int(input())
    for i in range(1, t + 1):
        n_str, m_str = input().split(" ")
        models = []
        for j in range(int(m_str)):
            model_char, row_str, col_str = input().split(" ")
            models.append((model_char, int(row_str), int(col_str)))
        cases.append((int(n_str), models))

    pool = multiprocessing.Pool()
    results = pool.starmap(answer, cases)
    pool.close()

    for (result, changes), i in zip(results, range(1, t + 1)):
        print("Case #{}: {} {}".format(i, result, len(changes)))
        for model_char, row_str, col_str in changes:
            print("{} {} {}".format(model_char, row_str, col_str))


if __name__ == "__main__":
    main()
