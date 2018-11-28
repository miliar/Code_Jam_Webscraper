def get_line():
    return raw_input().strip("\n")

def determine_time_to_win(goal, farm_price, farm_rate, cookie_rate=2.0, base_time=0.0):
    while True:
        time_until_win = goal / cookie_rate
        time_until_farm = farm_price / cookie_rate
        time_until_win_with_farm = time_until_farm + (goal / (cookie_rate + farm_rate))
        if time_until_win <= time_until_win_with_farm:
            return base_time + time_until_win
        else:
            base_time += time_until_farm
            cookie_rate += farm_rate

num_cases = int(get_line())
for case in xrange(1, num_cases + 1):
    parts = get_line().split(" ")
    farm_price, farm_rate, goal = map(float, parts)
    answer = determine_time_to_win(goal, farm_price, farm_rate)
    print "Case #%s: %.7f" % (case, answer)
