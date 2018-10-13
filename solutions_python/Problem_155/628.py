

def solve_problem(s_max, shyness):
    cur_standing = 0
    needed_extra = 0
    for i in range(len(shyness)):
        #print(i, cur_standing, needed_extra)
        if cur_standing < i:
            needed_extra += 1
            cur_standing += 1
        cur_standing += shyness[i]

    return needed_extra


if __name__ == '__main__':
    with open('d:\_Projects\GoogleCodeJam\inp\A-large.in', 'r') as inp_file:
        all_lines = inp_file.readlines()

    n = int(all_lines[0])
    tasks = []
    for test in all_lines[1:]:
        splt = test.replace('\n', '').split(' ')
        s_max = int(splt[0])
        shyness = [int(x) for x in list(splt[1])]

        tasks.append((s_max, shyness))

    #solve_problem(tasks[2][0], tasks[2][1])
    with open('d:\_Projects\GoogleCodeJam\inp\A-large.out', 'w+') as out_file:
        for i in range(len(tasks)):
            res = solve_problem(tasks[i][0], tasks[i][1])
            out_file.write('Case #{0}: {1}\n'.format(i+1, res))