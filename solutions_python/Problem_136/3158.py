import sys
curr_case = 1
input_list = sys.stdin.readlines()
max_case = int(input_list[0])
input_list.pop(0)

def getCookieRate(f, f_multiplier):
    return f*f_multiplier + 2

while (curr_case <= max_case):
    cfx_terms = input_list[0].split()
    c = float(cfx_terms[0])
    f = float(cfx_terms[1])
    x = float(cfx_terms[2])
    time_so_far = 0
    f_multiplier = 0
    cookie_rate = getCookieRate(f, f_multiplier)
    old_time = x/cookie_rate
    new_time = 0
    while (old_time > new_time):
        time_to_next_farm = c/cookie_rate
        f_multiplier += 1
        new_cookie_rate = getCookieRate(f, f_multiplier)
        time_to_goal = x/new_cookie_rate
        new_time = time_to_next_farm + time_to_goal
        if old_time > new_time:
            old_time = time_to_goal
            cookie_rate = new_cookie_rate
            time_so_far += time_to_next_farm
            new_time = 0
    else: 
        total_time = time_so_far + x/cookie_rate
        print "Case #%s:" % (curr_case), total_time
    input_list.pop(0)
    curr_case = curr_case + 1
