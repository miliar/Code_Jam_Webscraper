f_in = open('C-small-attempt0.in')
f_out = open('C-small.out', 'w')

T = int(f_in.readline())

def read_ints():
    return [int(x) for x in f_in.readline().rstrip().split()]

def solve():
    N, Q = read_ints()  # no. horses/cities, no. pairs of stops
    # horses/cities are 1 indexed
    horses = []  #  max dist, speed
    for i in range(N):
        horses.append(read_ints())
    distances = []
    for i in range(N):
        distances.append(read_ints())
    U, V = read_ints()

    def faster(curr_city, curr_horse):
        if curr_city == N - 1:
            # reached the end
            return 0.0
        # compare: keep horse or switch horse
        distance = distances[curr_city][curr_city + 1]

        curr_horse_remaining = horses[curr_horse[0]][0] - curr_horse[1]
        new_horse_remaining = horses[curr_city][0]

        if curr_horse_remaining < distance and new_horse_remaining < distance:
            return None  # impossible

        curr_horse_time = None
        new_horse_time = None

        if curr_horse_remaining >= distance:
            rest_of_time = faster(curr_city + 1, (curr_horse[0], curr_horse[1] + distance))
            if rest_of_time is not None:
                curr_horse_time = distance * 1.0/horses[curr_horse[0]][1]  + rest_of_time

        if new_horse_remaining >= distance:
            rest_of_time = faster(curr_city + 1, (curr_city, distance))
            if rest_of_time is not None:
                new_horse_time = distance * 1.0/horses[curr_city][1]  + rest_of_time

        if curr_horse_time is None:
            return new_horse_time
        elif new_horse_time is None:
            return curr_horse_time
        else:
            return min(curr_horse_time, new_horse_time)

    return faster(1, (0, distances[0][1])) + distances[0][1] * 1.0 / horses[0][1]



for case in range(1, T+1):
    out = 'Case #{}: {}\n'.format(case, solve())
    f_out.write(out)
    print out




f_in.close()
f_out.close()
