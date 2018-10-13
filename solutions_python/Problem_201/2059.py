from math import log2, floor, ceil

def parse_input():
    data = []
    with open('C-large.in', 'r') as f:
        for line in f:
            data.append(line.strip('\n'))
    T = int(data[0])
    cases = []
    for i in range(T):
        stalls, people = data[1 + i].split(" ")
        cases.append((int(stalls), int(people)))
    return T, cases


def solve_case(case):
    # print(case)
    stalls, people = case

    if stalls == people:
        return 0, 0

    if people >= 200:
        y = floor(log2(stalls))
        j = stalls - 2**y + 2**(y-1) + 1
        if j > 2**y:
            j = 2**y

        # print("J: {}   people: {}   stalls:{}".format(j, people, stalls))

        if people >= j:
            return 0, 0

        # if stalls < 2**y + 2**(y-1):
        #     d = 2**(y - 1)
        # else:
        #     d = stalls - 2**y
        # if people >= d:
        #     return 1, 0
        #
        # y = floor(log2(stalls / 3))
        # if stalls < 4*2**y - 1:
        #     t = 2**y
        # else:
        #     t = stalls - 3*2**y + 1
        # if people >= t:
        #     return 1, 1
        #
        # y = floor(log2(stalls / 4))
        # if stalls < 5*2**y - 1:
        #     t = 2**y
        # else:
        #     t = stalls - 4*2**y + 1
        # if people >= t:
        #     return 2, 1

        p = 2

        while True:
            y = floor(log2(stalls / p))
            if stalls < (p+1)*2**y - 1:
                t = 2**y
            else:
                t = stalls - p*2**y + 1
            if people >= t:
                return ceil((p-1)/2), floor((p-1)/2)
            elif p == 500000000:
                raise ValueError("JIRI WAT")

            p += 1
    #
    #

    # indices = {}
    ind = [0, stalls+1]

    for p, person in enumerate(range(people)):
        max_diff = 0
        index = 0
        for i in range(len(ind) - 1):
            diff = ind[i+1] - ind[i]
            if diff > max_diff:
                max_diff = diff
                index = i
        new_value = ind[index] + max_diff//2
        a = new_value - ind[index] - 1
        b = ind[index+1] - new_value - 1
        # if max(a, b) == 0 and min(a, b) == 0:
        #     return p+1
        # print("{}: {} {}".format(p+1, max(a,b), min(a,b)))
        ind.insert(index+1, new_value)
    return max(a, b), min(a, b)

# for i in range(2, 1000):
#     print("{}: {}".format(i, solve_case((i, i-1))))
# print(solve_case((32, 15)))
# print(solve_case((6, 5)))
# print(solve_case((89, 26)))
#
T, cases = parse_input()
for c, case in enumerate(cases):
    attempts = solve_case(case)
    print('Case #{}: {} {}'.format(c + 1, attempts[0], attempts[1]))
