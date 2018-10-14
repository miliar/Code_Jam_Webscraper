
def main():
    file = open('A-large.in', 'rU')
    lines = iter(file.readlines())
    file.close()

    case_count = int(next(lines))

    for case_idx in range(case_count):

        distance, hors_count = [int(x) for x in next(lines).split()]

        longest_time = 0

        for hors_idx in range(hors_count):
            position, speed = [int(x) for x in next(lines).split()]
            remaining_distance = distance - position
            time = remaining_distance / speed
            if time > longest_time:
                longest_time = time

        max_speed = distance / longest_time

        print(f'Case #{case_idx  + 1}: {max_speed}')


if __name__ == '__main__':
    main()
