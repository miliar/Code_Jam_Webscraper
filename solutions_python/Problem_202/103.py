__author__ = 'Roberto'
import math

def finish(index, solution):

    print solution

    file_out.write("Case #{0}: {1}\n".format(index+1, solution))
    debug_out.write("{0}\n".format( solution))

def is_bishop_collision(bishop_a, bishops):

    for bishop in bishops:
        if (bishop_a[0] + bishop_a[1]) == (bishop[0] + bishop[1]) or (bishop_a[0] - bishop_a[1]) == (bishop[0] - bishop[1]):
            return True

    return False

def print_board(N, rooks, bishops):

    for i in xrange(1, N + 1):
        for j in xrange(1, N + 1):
            if (i, j) in bishops:
                if (i, j) in rooks:
                    print "o",
                else:
                    print "+",
            elif (i, j) in rooks:
                print "x",
            else:
                print ".",
        print

def rook_arrangement(N, rooks, start_i):

    for i in xrange(start_i, N + 1):
        for j in xrange(1, N + 1):
            if not any(x == i or y == j for x, y in rooks):
                new_rooks = rooks[:]
                new_rooks.append((i, j))
                future_arrangement = rook_arrangement(N, new_rooks, i)
                if len(future_arrangement) == N:
                    return future_arrangement

    return rooks[:]

def solve_test(index, N, models):

    debug_out.write("Case #{0} In: {1}, {2} Out: ".format(index, N, ",".join(models)))

    print "Case: [{0}, {1}]".format(N, ",".join(models))

    bishop_models = []
    rook_models = []
    for model in models:
        model_type, x, y = model.split()
        x = int(x)
        y = int(y)

        if model_type == "+" or model_type == "o":
            bishop_models.append((x, y))
        if model_type == "x" or model_type == "o":
            rook_models.append((x, y))

    final_bishop_models = [(1, c) for c in xrange(1, N + 1)]
    final_bishop_models.extend([(N, c) for c in xrange(2, N)])

    for bishop in final_bishop_models[:]:
        if is_bishop_collision(bishop, bishop_models):
            final_bishop_models.remove(bishop)

    final_bishop_models.extend(bishop_models)

    final_rook_models = rook_arrangement(N, rook_models, 1)

    score = len(final_rook_models) + len(final_bishop_models)
    queen_models = [model for model in final_bishop_models if model in final_rook_models]

    for model in queen_models: final_rook_models.remove(model)
    for model in queen_models: final_bishop_models.remove(model)

    added_models = []
    for model in queen_models:
        if model not in rook_models or model not in bishop_models:
            added_models.append("o {0} {1}".format(model[0], model[1]))

    for model in final_rook_models:
        if model not in rook_models:
            added_models.append("x {0} {1}".format(model[0], model[1]))

    for model in final_bishop_models:
        if model not in bishop_models:
            added_models.append("+ {0} {1}".format(model[0], model[1]))

    result_lines = []
    result_lines.append("{0} {1}".format(score, len(added_models)))
    if len(added_models) > 0:
        result_lines.append("\n".join(added_models))
    finish(index, "\n".join(result_lines))


if __name__ == "__main__":
    task = "D"
    level = 1
    attempts = 0

    if level == 0:
        file_name = "sample.in"
    elif level == 1:
        file_name = "{0}-small-attempt{1}.in".format(task, attempts)
    else:
        file_name = "{0}-large.in".format(task)



    file_out_name = file_name.replace("in", "out")
    file_out = open(file_out_name, 'w')
    debug_out = open(file_name.replace("in", "debug"), 'w')

    with open(file_name, 'r') as file:
        content = file.read()

    lines = content.split('\n')
    number_of_lines = int(lines[0])

    test_cases = lines[1:]

    iter = 0
    for i in xrange(0, number_of_lines):

        N, M = map(int, test_cases[iter].split())
        solve_test(i, N, test_cases[iter + 1:iter + 1 + M])

        iter += M + 1

    file_out.close()