def cookie_clicker(filename):
    with open(filename, 'r') as f:
        t = int(f.readline())

        cases = list(map(lambda line: line.strip().split(' '), f))

        for i, case in enumerate(cases):
            print("Case #" +  str(i + 1) + ":", solve(case))

def solve(case):
    c, f, x = float(case[0]), float(case[1]), float(case[2])

    times = []

    cps = 2
    i = 0
    elapsed_time = 0

    while True:
        time_taken = x / cps + elapsed_time
        # print(cps, time_taken, elapsed_time)
        # print(times)
        if times and time_taken > times[-1]:
            break
        times.append(time_taken)

        elapsed_time += c / cps
        cps += f
        i += 1

    return min(times)

if __name__ == '__main__':
    # cookie_clicker('cookie_clicker_sample.in')
    # cookie_clicker('B-small-attempt0.in')
    cookie_clicker('B-large.in')



