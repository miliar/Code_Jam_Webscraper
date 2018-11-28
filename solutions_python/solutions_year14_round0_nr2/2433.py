def parse(name):
    in_file = open('%s.in' % name, 'r')
    cases = int(in_file.readline())
    lines = []
    for case in range(1, cases + 1):
        c, f, x = [float(x) for x in in_file.readline().split()]
        solution = solve(c, f, x)
        lines.append('Case #%s: %s\n' % (case, solution))
    in_file.close()
    out_file = open('%s.out' % name, 'w')
    out_file.writelines(lines)
    out_file.close()

def solve(farm_cost, farm_output, goal):
    farm_count = 0
    running_time = 0.0
    while True:
        rate = farm_count * farm_output + 2
        time_to_win = goal / rate
        time_to_build = farm_cost / rate
        if time_to_win < time_to_build:
            running_time += time_to_win
            break
        else:
            farm_count += 1
            new_rate = farm_count * farm_output + 2
            new_time_to_win = goal / new_rate
            if time_to_win < time_to_build + new_time_to_win:
                running_time += time_to_win
                break
            else:
                running_time += time_to_build
    return '%.7f' % running_time

parse('B-large')
