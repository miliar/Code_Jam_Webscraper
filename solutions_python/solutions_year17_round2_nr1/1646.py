# -*- coding: utf-8 -*-


import click


@click.command()
@click.argument('input_file', type=click.File())
@click.argument('output_file', type=click.File(mode='w'))
def main(input_file, output_file):
    # Read in the number of cases first
    num_cases = int(input_file.readline())

    for i in range(1, num_cases + 1):
        # Solve the case
        result = solve_line(input_file)
        # Print the output
        click.echo('Case #{}: {}'.format(i, result), file=output_file)


def solve_line(input_file):
    spl = input_file.readline().split()
    d = int(spl[0])
    n = int(spl[1])

    # print(d)

    other_horses = []

    for _ in range(n):
        spl = input_file.readline().strip().split()
        other_horses.append(tuple(int(x) for x in spl))

    other_horses.sort()

    total_time = 0

    i = 0
    current_distance = other_horses[0][0]

    while i < n:
        # print(total_time)

        initial, speed = other_horses[i]

        caught_up = False

        for j in range(i + 1, n):
            next_initial, next_speed = other_horses[j]
            # figure out what distance this horse will catch up with the next one
            try:
                catch_up_time = (next_initial - initial) / (speed - next_speed)
            except ZeroDivisionError:
                catch_up_time = 0
            catch_up_distance = initial + catch_up_time * speed

            if next_initial <= catch_up_distance < d:
                # The horse will catch up.
                # add in the time it takes for the horse to catch up
                total_time += ((catch_up_distance - initial) / speed)
                caught_up = True
                current_distance = catch_up_distance
                i = j
                break

        if not caught_up:
            # Just add in the time it takes for this horse to reach the end since it never
            # caught up to any other horses
            # print(initial)
            total_time += ((d - current_distance) / speed)
            break

    return d / total_time

# s * x + i = y


# s1 * x + i1 == s2 * x + i2
# (s1 - s2) * x == i2 - i1
# x = (i2 - i1) / (s1 - s2)


# speed = distance / time
# time * speed = distance
# time = distance / speed


if __name__ == '__main__':
    main()
