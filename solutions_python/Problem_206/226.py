# pylint: disable=missing-docstring
import sys


def problem(distance, num, horses):
    max_time = 0
    for horse in horses:
        time = (distance - horse[0]) / horse[1]
        max_time = max(time, max_time)
    return distance / max_time

def nextline(input_file):
    data = ""
    while not data:
        data = input_file.readline()
    return data[:-1]


def main():
    result = ""
    with sys.stdin if len(sys.argv) == 1 else open(sys.argv[1], 'r') as infile:
        number = int(nextline(infile))
        for run in range(number):
            case = nextline(infile)
            distance, num = [int(x) for x in case.split(" ")]
            horses = []
            for _ in range(num):
                horse = nextline(infile)
                horse = [int(x) for x in horse.split(" ")]
                horses.append(horse)
            result += 'Case #{}: {}\n'.format(1 + run, problem(distance, num, horses))

    if len(sys.argv) == 1:
        print(result, end='')
    else:
        with open(sys.argv[1].replace('in', 'sol'), 'w') as result_file:
            result_file.write(result)

if __name__ == '__main__':
    main()
