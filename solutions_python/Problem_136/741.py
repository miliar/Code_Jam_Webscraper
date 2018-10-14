__author__ = 'Adela'


def main():
    t = int(input())

    for i in range(t):
        c, f, x = (float(k) for k in input().split())
        rate = 2.0
        threshold = f * (x - c) / c

        time_needed = 0.0
        if threshold < rate:
            time_needed = x / rate
        else:
            nr_farms = int((threshold - rate)/f) + 1
            for j in range(nr_farms):
                time_needed += c/rate
                rate += f
            time_needed += x / rate

        print("Case #", i+1, ": ", time_needed, sep='')





if __name__ == "__main__":
    main()
