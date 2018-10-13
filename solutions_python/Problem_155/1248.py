#!/usr/bin/env python


def process_people(people):
    standing = 0
    min_people_needed = 0
    for s_i, num_people in enumerate(people):
        num_people = int(num_people)
        if num_people == 0:
            continue
        elif s_i == standing:
            standing += num_people
        else:
            diff = s_i - standing
            standing += num_people
            if diff > min_people_needed:
                min_people_needed = diff

    return min_people_needed


if __name__ == '__main__':
    with open('large.in', 'r') as infile:
        with open('large_output.txt', 'w') as outfile:
            cases = int(infile.readline().strip())

            for i in range(cases):
                case = i + 1
                line = infile.readline().strip()
                _, people = line.split()
                extra_people = process_people(people)
                outfile.write('Case #{}: {}\n'.format(case, extra_people))
