import sys


def main():
    cases = int(raw_input())
    for case in range(cases):
        cities, stops = map(int, raw_input().split(" "))
        city_data = []
        for city in range(cities):
            horse_km, horse_speed = map(int, raw_input().split(" "))
            city_data.append([horse_speed, horse_km, None])
        for city in range(cities-1):
            city_data[city][2] = map(int, raw_input().split(" "))[city + 1]
        last_city = raw_input()
        for stop in range(stops):
            raw_input()
        sol = solve(city_data)
        print "Case #%d: %s" % (case + 1, sol)

def solve(city_data):
    time_to_end = [0] * len(city_data)


    for current_city in range(len(city_data))[::-1][1:]:
        horse_speed, horse_km, dist = city_data[current_city]
        if horse_km < dist:
            continue

        km_left = horse_km
        t_city = current_city+1
        best = []
        time_so_far = 0
        while t_city < len(city_data):
            km_left -= city_data[t_city-1][2]
            if km_left < 0:
                break
            time_took = float(horse_km - km_left) / horse_speed
            best.append(time_took + time_to_end[t_city])
            t_city += 1
        
        time_to_end[current_city] = min(best)

    return time_to_end[0]
            


if __name__ == "__main__":
    main()
    # main()
