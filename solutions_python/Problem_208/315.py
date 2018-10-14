import heapq as hq


def solve(N, Q, horse_distances, horse_speeds, city_distances, pairs):
    out = []
    for start_city, end_city in pairs:
        start_city -= 1
        end_city -= 1
        # tup = (time, city_id, current_horse_distance_remain, current_horse_speed)
        heap = [(0., start_city, 0., 1.)]
        reached_cities = set()
        reached_cities_top_horses = dict()
        while True:
            time, city_id, current_horse_distance_remain, current_horse_speed = hq.heappop(heap)
            if city_id == end_city:
                break
            if city_id in reached_cities:
                good_horse = False
                for top_horse_dist, top_horse_speed in reached_cities_top_horses[city_id]:
                    if current_horse_distance_remain > top_horse_dist or current_horse_speed > top_horse_speed:
                        good_horse = True
                if good_horse is False:
                    continue
                new_top_horses = [(current_horse_distance_remain, current_horse_speed)]
                for top_horse in reached_cities_top_horses[city_id]:
                    if top_horse[0] > current_horse_distance_remain or top_horse[1] > current_horse_speed:
                        new_top_horses.append(top_horse)
                reached_cities_top_horses[city_id] = new_top_horses
            else:
                reached_cities.add(city_id)
                reached_cities_top_horses[city_id] = [(current_horse_distance_remain, current_horse_speed)]

            new_horse_d = horse_distances[city_id]
            new_horse_s = horse_speeds[city_id]
            for to_id, dist in enumerate(city_distances[city_id]):
                if dist == -1:
                    continue
                if dist <= current_horse_distance_remain:
                    hq.heappush(heap, (time + dist * 1. / current_horse_speed, to_id, current_horse_distance_remain - dist, current_horse_speed))
                if dist <= new_horse_d:
                    hq.heappush(heap, (time + dist * 1. / new_horse_s, to_id, new_horse_d - dist, new_horse_s))
        out.append(str(time))
    return ' '.join(out)


if __name__ == "__main__":
    output = []
    fname = 'C-small-attempt2'
    with open(fname + '.in') as f:
        inputs = [line.strip() for line in f]

    num_cases = int(inputs[0])
    line = [1]

    def next_line():
        text = inputs[line[0]]
        line[0] += 1
        return text

    for i in range(num_cases):
        N, Q = map(int, next_line().split())
        horse_distances = []
        horse_speeds = []
        for _ in range(N):
            dist, speed = map(int, next_line().split())
            horse_distances.append(dist)
            horse_speeds.append(speed)
        city_distances = []
        for _ in range(N):
            city_distances.append(list(map(int, next_line().split())))
        pairs = []
        for _ in range(Q):
            u, v = map(int, next_line().split())
            pairs.append((u, v))

        print(i + 1)
        output.append("Case #%d: " % (i + 1) + str(solve(N, Q, horse_distances, horse_speeds, city_distances, pairs)))

    with open(fname + '.out', 'w') as f:
        f.write('\n'.join(output))
