'''
Created on Apr 12, 2014

@author: youssefhassan
'''


class Round:
    def __init__(self, c, f, x):
        self.c = c
        self.f = f
        self.x = x 

num_of_test_cases = -1
rounds = []
def load_data():
    f = open("B-small-attempt0.in.in")
    num_of_test_cases = int(f.readline())
    for line in f.readlines():
        content = [float(x)  for x in line.split(' ')]
        rounds.append(Round(content[0], content[1], content[2]))
        

load_data()

case_number = 0
for play in rounds:
    case_number += 1
    num_cookies = 0
    seconds = 0.0
    cookies_rate = 2
    farms = 0
    EPSILON = 10 ** -12
    while num_cookies + EPSILON< play.x:
    #    seconds += 0.1
    #    num_cookies += 0.1 * cookies_rate
        time_to_next_farm = (play.c - num_cookies) / cookies_rate
        time_to_x = (play.x - num_cookies) / cookies_rate
        seconds += min(time_to_next_farm,time_to_x)
        num_cookies += min(time_to_next_farm,time_to_x) * cookies_rate
        if num_cookies + EPSILON >= play.c:
            time_with_next_farm = (play.x - (num_cookies - play.c)) / (cookies_rate+play.f)
            time_without_next_farm = (play.x - num_cookies) / cookies_rate
            if time_without_next_farm > time_with_next_farm:
                cookies_rate += play.f
                num_cookies -= play.c
                farms += 1
            else:
                seconds += time_without_next_farm
                num_cookies += time_without_next_farm * cookies_rate
    output_text = 'Case #' + str(case_number) + ': '
    print output_text + str(seconds)
        
            