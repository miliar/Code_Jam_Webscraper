import sys


def main():
    cases = int(raw_input())
    for case in range(cases):
        dest_km, horses = map(int, raw_input().split(" "))
        locspeed = []
        for horse in range(horses):
            locspeed.append(tuple(map(int, raw_input().split(" "))))
        sol = solve(dest_km, locspeed)
        print "Case #%d: %f" % (case + 1, sol)

def solve(dest_km, locspeed):
    # print(dest_km, locspeed)
    horse_time = lambda horse: float(dest_km-horse[0])/horse[1]
    slowest_horse = max(locspeed, key=horse_time)
    slow_loc, slow_speed = slowest_horse
    new_speed = float(slow_loc)/horse_time(slowest_horse) + slow_speed
    return new_speed


if __name__ == "__main__":
    main()
