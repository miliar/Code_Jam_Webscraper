#! /usr/bin/env python

def timeToMinutes(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m


def trains(ifs):
    turnaround_time = int(ifs.readline())
    na, nb = map(int, ifs.readline().split())
    a_departure = []
    a_arrival = []
    b_departure = []
    b_arrival = []
    for i in range(na):
        departure, arrival = map(timeToMinutes, ifs.readline().split())
        a_departure.append(departure)
        a_arrival.append(arrival)
    for i in range(nb):
        departure, arrival = map(timeToMinutes, ifs.readline().split())
        b_departure.append(departure)
        b_arrival.append(arrival)
    count_a = 0
    tmp = sorted(b_arrival)
    for m in sorted(a_departure):
        if len(tmp) == 0 or m < tmp[0] + turnaround_time:
            count_a += 1
        else:
            tmp.pop(0)
    count_b = 0
    tmp = sorted(a_arrival)
    for m in sorted(b_departure):
        if len(tmp) == 0 or m < tmp[0] + turnaround_time:
            count_b += 1
        else:
            tmp.pop(0)
    return count_a, count_b


def main():
    ifs = open("B-large.in")
    ofs = open("out-b.txt", "w")
    num_cases = int(ifs.readline())
    for i in range(num_cases):
        start_at_a, start_at_b = trains(ifs)
        ofs.write("Case #%d: %d %d\n" % (i + 1, start_at_a, start_at_b))


if __name__ == "__main__":
    main()
