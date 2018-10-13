#!/usr/bin/env python2.7


PATH = 'problem-1-small-input.txt'


def get_shyness_counts_with_extra(shyness_counts, extra):
    for index, (shyness, count) in enumerate(shyness_counts):
        if index == 0:
            yield shyness, count + extra
        else:
            yield shyness, count

def will_everyone_stand(shyness_counts, extra=0):
    shyness_counts = get_shyness_counts_with_extra(shyness_counts, extra)
    people_standing, people_sitting = 0, 0
    for shyness, count in shyness_counts:
        if shyness <= people_standing:
            people_standing += count
        else:
            break
    else:
        return True
    return False


def compute_invitees(f):
    next(f)

    shynesses = (row.split(' ')[1][:-1] for row in f)
    operas = (
        [[index, int(n)] for index, n in enumerate(shyness)]
        for shyness in shynesses
    )

    for index, shyness_counts in enumerate(operas):
        for i in range(10000):
            if will_everyone_stand(shyness_counts, i):
                print "Case #{}: {}".format(index + 1, i)
                break


def main():
    with open(PATH) as f:
        compute_invitees(f)


if __name__ == '__main__':
    main()
