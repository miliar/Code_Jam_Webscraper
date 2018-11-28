from copy import copy


def solve_problem(pancakes):
    if pancakes[0] < 4:
        return pancakes[0]
    #print(pancakes)
    best_time = pancakes[0]
    for cut in range(2, pancakes[0]-1):
        new_pan = copy(pancakes)
        orig = new_pan[0]
        i = 0
        while new_pan[i] == orig:
            new_pan[i] -= cut
            new_pan.append(cut)
            i+=1
        time = solve_problem(sorted(new_pan, reverse=True)) + i
        if time < best_time:
            best_time = time

    return best_time


if __name__ == '__main__':
    with open('d:\_Projects\GoogleCodeJam\inp\B-small-attempt2.in', 'r') as inp_file:
        all_lines = inp_file.readlines()
    all_lines = [x.replace('\n', '') for x in all_lines]

    n = int(all_lines[0])
    tasks = []
    i = 1
    while i < len(all_lines):
        D = int(all_lines[i])
        pancakes = [int(x) for x in all_lines[i+1].split(' ')]
        tasks.append((D, pancakes))
        i += 2

    #solve_problem(tasks[2][0], tasks[2][1])
    with open('d:\_Projects\GoogleCodeJam\inp\OUT_B-small-attempt2.txt', 'w+') as out_file:
        for i in range(len(tasks)):
            print('task', i)
            res = solve_problem(sorted(tasks[i][1], reverse=True))
            out_file.write('Case #{0}: {1}\n'.format(i+1, res))
