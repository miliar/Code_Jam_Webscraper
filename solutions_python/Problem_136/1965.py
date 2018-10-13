base_cookie_rate = 2.0

def solve():
    farm_cost, farm_cookie_rate, win_cost = (float(num) for num in raw_input().split())
    time_spent = 0
    current_cookie_rate = base_cookie_rate
    time_to_win = win_cost / current_cookie_rate
    time_to_farm = farm_cost / current_cookie_rate
    time_to_win_with_farm = win_cost / (current_cookie_rate + farm_cookie_rate)
    while(time_to_farm + time_to_win_with_farm < time_to_win):
        time_spent += time_to_farm
        current_cookie_rate += farm_cookie_rate
        time_to_win = win_cost / current_cookie_rate
        time_to_farm = farm_cost / current_cookie_rate
        time_to_win_with_farm = win_cost / (current_cookie_rate + farm_cookie_rate)
    time_spent += time_to_win
    return "{:.7f}".format(time_spent)

cases = input()
output = []
for case in range(cases):
    output.append("Case #{}: {}".format(case + 1, solve()))
with open('output.txt', 'w') as file:
    file.write('\n'.join(output))