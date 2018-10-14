import fileinput

def find_arrive_time(D, horse):
    location, speed = horse
    return (D - location) / float(speed)

def solve(D, N, horses):
    #print horses

    # last_arrive = max(horses, lambda h: find_arrive_time(D, h))
    time = max(find_arrive_time(D, h) for h in horses)
    #print time, D/time
    return D / time

if __name__ == "__main__":
    f = fileinput.input()

    T = int(f.readline()) # Number of cases
    for case in xrange(1, T + 1):
        horses = []
        line = f.readline().strip()
        D, N = map(int, line.split(" "))

        for i in xrange(1, N+1):
            line = f.readline().strip()
            d, s = map(int, line.split(" "))
            horses.append((d,s))

        solution = solve(D, N, horses)

        print("Case #{0}: {1:f}".format(case, solution))