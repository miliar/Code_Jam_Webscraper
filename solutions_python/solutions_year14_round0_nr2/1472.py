INPUT_FILE = 'cookie_test.in'
OUTPUT_FILE = 'cookie_test.out'

in_file = open(INPUT_FILE, 'r')
out_file = open(OUTPUT_FILE, 'w')

n = int(in_file.readline())
case = 1

while n > 0:
    out_file.write('Case #' + str(case) + ': ')

    array = in_file.readline().split()

    farm_cost = float(array[0])     # cost to buy a farm, C
    add_cps = float(array[1])       # additional cps gained from farm, F
    goal = float(array[2])          # cookies needed to win, X

    time = 0        # total elapsed time
    cookies = 0     # number of cookies
    cps = 2         # cookies per second
    done = False

    while not done:
        time_until_farm = farm_cost/cps
        cookies += farm_cost
        time += time_until_farm

        no_farm_time_until_goal = (goal - cookies)/cps
        farm_time_until_goal = goal/(cps + add_cps)

        if no_farm_time_until_goal < farm_time_until_goal:
            time += no_farm_time_until_goal
            done = True
        else:
            cookies = 0
            cps += add_cps

    out_file.write(str(time) + '\n')

    n -= 1
    case += 1