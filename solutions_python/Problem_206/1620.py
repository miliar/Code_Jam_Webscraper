"""
if a horse at 2400/2525 is traveling at 5 km/h,
(2525-2400)/5 = 25 h
v = d/t, 2525/25 = 101

plan: find the horse that'll take the longest to get there,
and use that to calculate her speed
"""


def calculate(horses, total_distance):
    return '{0:.6f}'.format(total_distance / find_largest(horses, total_distance))


def find_largest(horses, total_distance):
    distance, speed = horses[-1].split(' ')
    time = (total_distance - int(distance)) / int(speed)
    if len(horses) == 1:
        return time
    else:
        return max(time, find_largest(horses[:-1], total_distance))


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    total_distance, horse_count = input().split(' ')
    horses = []
    for j in range(int(horse_count)):
        horses.append(input())
    print('Case #{}: {}'.format(i, calculate(horses, int(total_distance))))
