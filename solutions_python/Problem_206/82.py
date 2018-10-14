

def solve(horses, distance):
    time = 0
    for start, speed in horses:
        other_time = (distance - start) / speed
        time = max(time, other_time)
    return distance / time

def main():
    cases = int(input())
    for case in range(1, cases+1):
        distance, number_of_horses = tuple(int(x) for x in input().rstrip().split(" "))
        horses = []
        for _ in range(number_of_horses):
            horses.append(tuple(int(x) for x in input().rstrip().split(" ")))
        print("Case #%d: %s" % (case, solve(horses, distance)))

if __name__ == '__main__':
    main()

        