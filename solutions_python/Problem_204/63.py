import math

cases = input()


def calculate_valid_packages(total_quantity, serving_quantity):
    # print serving_quantity, total_quantity
    minimum_servings = int(math.floor(total_quantity / (serving_quantity * 1.1)))
    while minimum_servings * serving_quantity * 1.1 < total_quantity:
        minimum_servings += 1

    maximum_servings = int(math.ceil(total_quantity / (serving_quantity * 0.9)))
    while maximum_servings * serving_quantity * 0.9 > total_quantity:
        maximum_servings -= 1

    return minimum_servings, maximum_servings


for case in xrange(1, cases + 1):
    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = [sorted(map(int, raw_input().split())) for i in xrange(N)]

    # For each ingredient, calculate the minimum and maximum packages
    valid_packages = [[calculate_valid_packages(Q[i][j], R[i]) for j in xrange(P)] for i in xrange(N)]

    Q_positions = [0] * N
    solution = 0

    # print valid_packages

    while not any([Q_positions[i] == P for i in xrange(N)]):
        # print Q_positions

        servings_mins = [valid_packages[i][Q_positions[i]][0] for i in xrange(N)]
        servings_maxs = [valid_packages[i][Q_positions[i]][1] for i in xrange(N)]

        min_servings = max(servings_mins)
        max_servings = min(servings_maxs)

        if min_servings > max_servings:
            # Not possible, increment positions
            for i in xrange(N):
                if valid_packages[i][Q_positions[i]][1] == max_servings:
                    Q_positions[i] += 1
            continue

        # Okay, add bundle
        solution += 1

        for i in xrange(N):
            Q_positions[i] += 1


    print 'Case #%d: %d' % (case, solution)