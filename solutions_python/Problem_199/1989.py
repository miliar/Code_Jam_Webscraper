def parse_input():
    data = []
    with open('A-small-attempt0 (1).in', 'r') as f:
        for line in f:
            data.append(line.strip('\n'))
    T = int(data[0])
    cases = []
    for i in range(T):
        plate, num = data[1 + i].split(" ")
        cases.append((plate, int(num)))
    return T, cases


def swap(case, index):
    plate, size = case
    p = list(plate)
    for i in range(size):
        p[index + i] = '-' if plate[index+i] == '+' else '+'
    return "".join(p), size


def solve_case(case, cases_done=None, parent=None):
    if cases_done is None:
        cases_done = {}
    plate, size = case
    cases_done[case] = 'IMPOSSIBLE'

    if '-' not in plate:
        return 0

    if plate.count('-') % 2 == 1 and size % 2 == 0:
        return 'IMPOSSIBLE'

    min_attempts = 9999999
    for i in range(len(plate)):
        if len(plate) - i < size:
            break

        next_case = swap(case, i)
        if next_case == parent:
            continue
        if next_case in cases_done:
            attempts = cases_done[next_case]
        else:
            attempts = solve_case(next_case, cases_done, case)
            cases_done[next_case] = attempts

        if attempts == 'IMPOSSIBLE':
            continue
        else:
            attempts += 1

        if attempts < min_attempts:
            min_attempts = attempts

    if min_attempts == 9999999:
        min_attempts = 'IMPOSSIBLE'
    return min_attempts


# def solve_case(case):
#     plate, size = case
#     if plate.count('-') % 2 == 1 and size % 2 == 0:
#         return 'IMPOSSIBLE'

#     attempts = 0
#     while True:
#         isize = plate.count('-' * size)
#         if isize > 0:
#             plate = plate.replace('-' * size, '+' * size)
#             attempts += isize
#         else:
#             ppattern = '-{}-'.format('+' * (size-1))
#             psize = plate.count(ppattern)
#             if psize > 0:
#                 plate = plate.replace(ppattern, '+'*(size+1))
#                 attempts += psize * 2
#             else:
#                 break
#     if '-' in plate:
#         attempts = 'IMPOSSIBLE'
#     return attempts

T, cases = parse_input()
for c, case in enumerate(cases):
    attempts = solve_case(case)
    print('Case #{}: {}'.format(c+1, attempts))
