__author__ = 'sean223'


# IN_FILE = 'test_input.txt'
# OUT_FILE = 'test_output.txt'

# IN_FILE = 'C-small-1.in'
# OUT_FILE = 'small_1_out.txt'

# IN_FILE = 'C-small-2.in'
# OUT_FILE = 'small_2_out.txt'

IN_FILE = 'C-large.in'
OUT_FILE = 'large_out.txt'


with open(IN_FILE, 'r') as fileIn:
    fileLines = fileIn.readlines()

it = iter(fileLines)
numbCases = int(next(it))
output = ""


def iterate(first, second, first_quantity, second_quantity):
    if first_quantity < 1:
        raise Exception("First Quantity is assumed to be positive")
    if second_quantity == 0:
        if first % 2 == 1:
            return first//2, 0, 2*first_quantity, 0
        else:
            return first//2, (first-1)//2, first_quantity, first_quantity
    else:
        if not first == second+1:
            raise Exception("First is assumed to be second+1")
        if first % 2 == 1:
            return first//2, first//2 - 1, 2*first_quantity+second_quantity, second_quantity
        else:
            return first//2, first//2 - 1, first_quantity, first_quantity+2*second_quantity

for case in range(1, numbCases+1):
    n, k = [int(x) for x in next(it).strip().split(' ')]

    # intervals = [n]
    #
    # for i in range(k-1):
    #     (minimum, index) = max((minimum, index) for (index, minimum) in enumerate(intervals))
    #     if minimum == 1:
    #         break
    #     elif minimum == 2:
    #         intervals[index] = 1
    #     else:
    #         intervals[index] = (minimum-1)//2
    #         intervals.insert(index+1, minimum//2)
    #
    # (minimum, index) = max((minimum, index) for (index, minimum) in enumerate(intervals))
    # min_lr = (minimum-1) // 2
    # max_lr = minimum // 2

    a, b, qa, qb = n, 0, 1, 0
    iterations = 0
    while 2**iterations <= k:
        iterations += 1
        a, b, qa, qb = iterate(a, b, qa, qb)

    steps = k - 2**(iterations-1) + 1
    loop_around = steps + 2**(iterations-1)

    max_lr, min_lr = 0, 0
    if steps <= qa and loop_around <= qa:
        max_lr, min_lr = a, a
    elif steps <= qa:
        max_lr, min_lr = a, b
    else:
        max_lr, min_lr = b, b

    line = "Case #{0}: {1}\n".format(str(case), str(max_lr) + ' ' + str(min_lr))
    output += line


with open(OUT_FILE, 'w') as fileOut:
    fileOut.write(output)
