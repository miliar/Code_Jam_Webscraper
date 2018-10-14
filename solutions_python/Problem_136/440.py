# coding=utf-8 *** gatopeich for Google Code Jam 2014

# Problem B. Cookie Clicker Alpha

filename = 'B-large'

next_line = open(filename+'.in').readline

T = int(next_line())
print(T, "cases")

out = open(filename+'.out', 'w')
for case in range(1, T+1):
    C, F, X = map(float, next_line().split())

    time = 0.0
    cookies = 0.0
    rate = 2.0

    while True:
        time_left = X/rate
        farm_cost = C/rate
        if time_left <= farm_cost:
            break
        if time_left > (X/(rate+F)) + farm_cost:
            time += farm_cost
            rate += F
        else:
            break

    time += time_left

    print('Case #%d:'%case, time, file=out)

out.close()

