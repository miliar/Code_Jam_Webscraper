import fileinput

num_inputs = 0
lines = []

for line in fileinput.input():
    lines.append(line)

num_inputs = int(lines[0])

for i in range(1,num_inputs+1):
    nums = lines[i].split(' ')
    cookies_per_second = 2.0
    seconds_elapsed = 0
    farm_cost = float(nums[0])
    cps_per_farm = float(nums[1])
    goal = float(nums[2])

    seconds = goal / cookies_per_second
    seconds_with_farm = farm_cost / cookies_per_second + goal / (cookies_per_second + cps_per_farm)
    while(seconds > seconds_with_farm):
        seconds_elapsed += farm_cost/cookies_per_second
        cookies_per_second += cps_per_farm
        seconds = goal / cookies_per_second + seconds_elapsed
        seconds_with_farm = farm_cost / cookies_per_second + goal / (cookies_per_second + cps_per_farm) + seconds_elapsed

    print('Case #'+str(i)+': {0:.7f}'.format(seconds))
        
