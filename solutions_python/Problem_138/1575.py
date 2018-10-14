from __future__ import print_function, division
import copy
import sys

# infile = open(sys.argv[1])
# outfiles = (sys.stdout, open(sys.argv[2], 'w'))
infile = open("d_large.txt")
outfiles = (sys.stdout, open("d_out_large.txt", 'w'))


def read_in(infile):
    content = []
    data = infile.readlines()
    amount = int(data[0])
    for idx in xrange(1, amount*3+1, 3):
        array1 = data[idx + 1: idx + 2][0].split()
        array1 = [float(f) for f in array1]
        # array1.sort()

        array2 = data[idx + 2: idx + 3][0].split()
        array2 = [float(f) for f in array2]
        # array2.sort()

        content.append((array1, array2))
    assert amount == len(content)
    return content


def do_output(number, output, outfiles):
    for f in outfiles:
        print('Case #%d:' % number, output, file=f)


def main():
    for i, content in enumerate(read_in(infile)):
        do_output(i+1, do_task(content), outfiles)


def nextof(arr, value, smaller=False):
    array = copy.deepcopy(arr)
    array.sort()
    val = 0
    try:
        if smaller:
            array.reverse()
            val = next(v for i, v in enumerate(array) if v < value)
        else:
            val = next(v for i, v in enumerate(array) if v > value)
    except StopIteration, e:
        if smaller:
            val = min(array)
        else:
            val = max(array)
    return val

def play_war(Naomi, Ken):
    naomi = copy.deepcopy(Naomi)
    ken = copy.deepcopy(Ken)

    ken.sort()

    points = 0

    for i in xrange(len(naomi)):
        n = naomi.pop()
        k_max = max(ken)
        k_min = min(ken)
        if n < k_min or n > k_max:
            k = ken.pop(ken.index(k_min))
        else:
            k = ken.pop(ken.index(nextof(ken, n)))
        if n > k:
            points += 1

    return points


def play_deceitful_war(Naomi, Ken):
    naomi = copy.deepcopy(Naomi)
    naomi.sort()
    ken = copy.deepcopy(Ken)
    ken.sort()
    points = 0

    print(naomi)
    print(ken)

    for i in xrange(len(naomi)):
        k_max = max(ken)
        k_min = min(ken)
        n_max = max(naomi)
        n_min = min(naomi)

        if n_max > k_max:
            # n_told = nextof(ken, k_max, smaller=True)
            n_told = k_max
            n = naomi.pop(naomi.index(nextof(naomi, k_max)))
        else:
            # n_told = nextof(naomi, k_max, smaller=True)
            n_told = n_min
            # while n_told not in naomi and n_told not in ken:
            # n = naomi.pop(naomi.index(n_min))
            supposed_k = nextof(ken, n_told)
            n = naomi.pop(naomi.index(nextof(naomi, supposed_k)))

        while True:
            if n_told >= 1.0 or n_told >= k_max:
                n_told -= 0.00001
            else:
                n_told += 0.00001
            if n_told not in naomi and n_told not in ken:
                break

        if n_told < k_min or n_told > k_max:
            k = ken.pop(ken.index(k_min))
        else:
            k = ken.pop(ken.index(nextof(ken, n_told)))

        if n > k:
            points += 1

    return points


def do_task(content):

    dwar_points = 0      # points received for deceitful war game
    war_points = 0       # points received for war game

    naomi = content[0]   # Naomi's blocks (sorted)
    ken = content[1]     # Ken's blocks (sorted)

    print('original naomi:', naomi)
    print('original ken:  ', ken)

    dwar_points = play_deceitful_war(naomi, ken)
    war_points = play_war(naomi, ken)

    return '{0} {1}'.format(dwar_points, war_points)


if __name__ == '__main__':
    main()
