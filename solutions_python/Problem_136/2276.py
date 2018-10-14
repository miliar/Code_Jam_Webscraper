# cookieclicker.py
# Google Code Jam 2014
# Chad Gibbons, dcgibbons@gmail.com

import fileinput

file_input = fileinput.input()
T = int(file_input.readline())

for test_case in range(1, T+1):
    line = file_input.readline().rstrip().split(' ')
    C = float(line[0]) # farm_cost
    F = float(line[1]) # farm rate
    X = float(line[2]) # total cookie goal

    cookies_per_second = 2.
    current_cookies = 0.
    total_seconds = 0.

    while current_cookies < X:
        seconds_needed_for_farm = C / cookies_per_second
        seconds_needed_for_goal = (X - current_cookies) / cookies_per_second
        seconds_needed_for_goal2 = seconds_needed_for_farm + (X / (cookies_per_second+F))
        if seconds_needed_for_goal2 < seconds_needed_for_goal:
            total_seconds += seconds_needed_for_farm
            current_cookies += seconds_needed_for_farm * cookies_per_second
            # buy a farm!
            current_cookies -= C
            cookies_per_second += F
        else:
            total_seconds += seconds_needed_for_goal
            current_cookies += seconds_needed_for_goal * cookies_per_second

    print "Case #%d: %.7f" % (test_case, total_seconds)
