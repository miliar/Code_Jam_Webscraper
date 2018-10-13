
def solve(distance, horses):
    max_t = 0
    for horse in horses:
        t = (distance - horse[0]) / horse[1]
        if t > max_t: max_t = t
    return distance / max_t

with open('large.txt') as f:
    num_cases = int(f.readline())
    for i in range(num_cases):
        first_line = f.readline().strip().split(' ')
        distance = float(first_line[0])
        horses = int(first_line[1])
        horse_init = []
        for j in range(horses):
            horse_line = [float(x) for x in f.readline().strip().split(' ')]
            horse_init.append(horse_line)

        result = solve(distance, horse_init)
        print "Case #{}: {}".format(i + 1, result)