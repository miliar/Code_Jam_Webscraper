def MushroomMonster():
    """
    For each test case, output one line containing "Case #x: y1, y2",
    where x is the test case number (starting from 1) and ys are
    the minimum number of mushrooms she must eat.
    """

    NUMB_TRIALS = raw_input()

    for trial in range(int(NUMB_TRIALS)):
        numb_intervals = int(raw_input())
        input_line = map(int, raw_input().split(' '))
        total_a, total_b = 0, 0
        consumption_rate = 0

        for index, plate_size in enumerate(input_line):
            if index + 1 < numb_intervals:
                diff = plate_size - input_line[index + 1]

                if diff > 0:
                    total_a += diff
                    consumption_rate = max(consumption_rate, diff)

        for index, plate_size in enumerate(input_line):
            if index + 1 == numb_intervals:
                break
            elif consumption_rate >= plate_size:
                total_b += plate_size
            else:
                total_b += consumption_rate


        print "Case #" + str(trial + 1) + ": " + str(total_a) + " " + str(total_b)

MushroomMonster()
