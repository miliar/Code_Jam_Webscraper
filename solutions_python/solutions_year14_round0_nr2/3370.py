def sec_to_goal(cps, cpf, farm_cps, goal_c, num_farms):
    if num_farms is 0:
        return goal_c / cps
    sec_to_goal = 0.0
    for x in range(num_farms):
        sec_to_farm = cpf / cps
        sec_to_goal += sec_to_farm
        cps += farm_cps
    sec_to_goal += goal_c / cps
    return sec_to_goal

fin = open('B-small-attempt0.in', 'r')
fout = open('output.out', 'w')
cases = int(fin.readline())
for case in range(1, cases + 1):
    cps = 2.0
    line = fin.readline().split(' ')
    cookies_per_farm = float(line[0])
    farm_cps = float(line[1])
    goal_cookies = float(line[2])
    min = float('inf')
    num_farms = 0

    while True:
        result = sec_to_goal(cps, cookies_per_farm,
                             farm_cps, goal_cookies, num_farms)
        num_farms += 1
        if result < min:
            min = result
        if result > min:
            break
        string = ("Case #" + str(case) + ": {0:.7f}".format(round(min, 7)))
    print(string)
    fout.write(string + "\n")
