import sys


def main():
    inputfh = sys.stdin
    outputfh = sys.stdout
    base_rate = 2.0
    for test_number in range(1, int(inputfh.readline().strip()) + 1):
        rate = base_rate
        farm_cost, farm_rate, needed = map(
            float, inputfh.readline().strip().split())
        time = 0.0
        while True:
            time_to_farm = farm_cost / rate
            time_to_total = needed / rate
            time_to_total_with_new_farm = time_to_farm + needed / (rate + farm_rate)
            if time_to_total <= time_to_total_with_new_farm:
                time += time_to_total
                break
            else:
                time += time_to_farm
                rate += farm_rate
        outputfh.write("Case #%d: %0.7f\n" % (test_number, time))


if __name__ == "__main__":
    main()
