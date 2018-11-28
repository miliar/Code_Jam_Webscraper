f_in = open("B-large.in", 'r')
f_out = open("b_real_large.out", 'w')

def get_int():
    return int(f_in.readline().rstrip())

def solve(C, F, X):
    cookies = 0.0
    rate = 2.0 # you start off producing 2 cookies per second
    time = 0.0

    while 1:
        # should buy farm or wait for goal?
        t_buy_farm = C / rate
        t_goal_with_farm = X / (rate + F) + t_buy_farm
        t_goal = X / rate
        if t_goal < t_goal_with_farm:
            time += t_goal
            return round(time, 9)
        else:
            time += t_buy_farm
            rate += F


T = get_int()

for case in range(1, T+1):
    bounds = f_in.readline().rstrip()
    floatbounds = [float(i) for i in bounds.split()]
    C, F, X = floatbounds
    # C = cost of farm
    # F = how much a farm generates
    # X = goal cookies
    f_out.write("Case #{0}: {1}\n".format(case, solve(C, F, X)))
        

f_in.close()
f_out.close()
