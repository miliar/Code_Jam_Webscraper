

def solve_problem(X, R, C):
    if R*C % X != 0:
        return False
    if R < X and C < X:
        return False
    if min(R,C) == 2:
        return X < 4
    if min(R,C) >= 2 and max(R,C) > 2:
        return True

    if X < 3:
        return True
    else:
        return False


if __name__ == '__main__':
    with open('d:\_Projects\GoogleCodeJam\inp\D-small-attempt3.in', 'r') as inp_file:
        all_lines = inp_file.readlines()
    all_lines = [x.replace('\n', '') for x in all_lines]

    n = int(all_lines[0])
    tasks = []
    for test in all_lines[1:]:
        splt = test.replace('\n', '').split(' ')
        X = int(splt[0])
        R = int(splt[1])
        C = int(splt[2])

        tasks.append((X, R, C))

    #solve_problem(tasks[2][0], tasks[2][1])
    with open('d:\_Projects\GoogleCodeJam\inp\OUT_D-small-attempt3.out', 'w+') as out_file:
        for i in range(len(tasks)):
            print('Task', i+1)
            res = solve_problem(tasks[i][0], tasks[i][1], tasks[i][2])
            str_out = 'GABRIEL' if res else 'RICHARD'
            out_file.write('Case #{0}: {1}\n'.format(i+1, str_out))