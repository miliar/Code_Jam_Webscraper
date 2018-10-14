# CodeJam 2017
# Jan Hartman, janh


def max_speed(distance, horses):

    slowest_horse, max_time = 0, 0
    for i, horse in enumerate(horses):
        pos, speed = horse
        time = (distance - pos) / speed

        if time > max_time or i == 0:
            slowest_horse = i
            max_time = time

    return distance / max_time


if __name__ == "__main__":
    test_cases = int(input())
    for case_no in range(test_cases):
        line = input().split(" ")
        d = int(line[0])
        n_horses = int(line[1])

        horses = []
        for horse in range(n_horses):
            line = input().split(" ")
            horses.append((int(line[0]), int(line[1])))

        print("Case #{:d}: {:f}".format(case_no + 1, max_speed(d, horses)))
