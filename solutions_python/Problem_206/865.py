from collections import namedtuple

def main(file):
    horse = namedtuple('horse', ['start', 'max_speed'])
    destination, num_horses = [int(i) for i in file.readline().split()]
    horses = []
    for _ in range(num_horses):
        stats = file.readline().split()
        horses.append(horse(int(stats[0]), int(stats[1])))
    prev_horse_time = 0
    for horse in horses:
        # If prev horse finishes before this one hits
        # finish, then we can just calculate straight.
        # Otherwise, it's time to hit the previous horse
        # location
        curr_horse_time = (destination - horse.start) / horse.max_speed
        if curr_horse_time > prev_horse_time:
            prev_horse_time = curr_horse_time
        else:
            continue
    return destination / prev_horse_time

if __name__ == '__main__':
    with open('A-small.out', 'w') as outfile:
        with open('A-small.in', 'r') as file:
            NUM_CASES = int(file.readline())
            for idx in range(1, NUM_CASES + 1):
                outfile.write("Case #{}: {:.6f}\n".format(idx, main(file)))
