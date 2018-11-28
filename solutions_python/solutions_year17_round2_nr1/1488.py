#!/usr/bin/python3

import sys


def main():
    with open('output', 'w') as output_file:
        with open(sys.argv[1]) as input_file:
            case_count = int(input_file.readline().strip('\n'))

            for case_number in range(1, case_count + 1):
                case_line = input_file.readline().strip('\n').split(' ')

                D = float(case_line[0])
                horse_count = int(case_line[1])
                horses = []

                for horse_number in range(0, horse_count):
                    horse_line = input_file.readline().strip('\n').split(' ')
                    horses.append((
                        float(horse_line[0]),
                        float(horse_line[1])
                    ))

                horses = horses

                # Do computations here
                first_horse_speed = get_optimal_speed(D, horses)
                first_horse_time = (D - horses[len(horses) - 1][0]) / first_horse_speed

                result = str(D / first_horse_time)

                output_file.write('Case #' + str(case_number) + ": " + result + '\n')


def get_optimal_speed(D, horses):

    opt_speed = None

    for i, horse in enumerate(horses):
        if i == 0:
            opt_speed = horse[1]
        else:
            ahead_speed = opt_speed
            ahead_time = (D - horses[i - 1][0]) / ahead_speed
            opt_speed = min(horse[1], (D - horses[i][0]) / ahead_time)

    return opt_speed


if __name__ == '__main__':
    main()
