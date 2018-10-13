import decimal


def answer(line):
    temp_line = line.split(" ")
    destination = decimal.Decimal(temp_line[0])
    num_other_horses = int(temp_line[1])
    horse_list = []
    for horse in range(num_other_horses):
        temp_horse = input().split(" ")
        temp_location = decimal.Decimal(temp_horse[0])
        temp_speed = decimal.Decimal(temp_horse[1])
        horse_list.append((destination - temp_location)/temp_speed)
    ##print(horse_list)
    horse_list = sorted(horse_list)
    worst_time = horse_list[-1]
    max_speed = destination / worst_time
    return max_speed
    ## Time to destination for horse:
    ##      Distance to destination / speed
    ## Speed of main horse = distance / time

def formatted(case_num, val):
    print("Case #{}: {}".format(case_num, val))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    temp_line = input()
    formatted(i, answer(temp_line))
