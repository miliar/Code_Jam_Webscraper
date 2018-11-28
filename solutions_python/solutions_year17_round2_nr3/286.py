# CodeJam 2017
# Jan Hartman, janh

import numpy as np


def ponies():
    time = 0.0
    return search(0, horses[0], time, horses[0][0])


def search(i_city, horse, total_time, endurance):
    if i_city == n - 1:
        return total_time

    # swap the horse or not
    dist_to_next = dists[i_city][i_city + 1]

    new_horse = horses[i_city]
    new_end, new_speed = new_horse
    new_total_time = total_time + dist_to_next / new_speed

    t2 = search(i_city+1, new_horse, new_total_time, new_end - dist_to_next)

    # swap
    if endurance < dist_to_next:
        return t2
    else:
        t1 = search(i_city+1, horse, total_time + dist_to_next / horse[1], endurance - dist_to_next)
        return min(t1, t2)


if __name__ == "__main__":
    test_cases = int(input())
    for case_no in range(test_cases):
        line = input().split(" ")
        n = int(line[0])
        q = int(line[1])

        horses = []
        dists = []
        pairs = []
        for i in range(n):
            line = input().split(" ")
            horses.append((int(line[0]), int(line[1])))

        for i in range(n):
            dists.append(list(map(lambda l: int(l), input().split(" "))))

        for i in range(q):
            line = input().split(" ")
            pairs.append((int(line[0]), int(line[1])))

        print("Case #{:d}: {:f}".format(case_no + 1, ponies()))
