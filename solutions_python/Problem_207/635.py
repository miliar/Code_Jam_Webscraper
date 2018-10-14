from copy import deepcopy


def which_index_max(li, ind):
    max = -1
    max_val = -1
    for i, val in enumerate(ind):
        if int(li[val]) >= max_val:
            max = val
            max_val = int(li[val])
    return max


def solve(lin):
    can_next = dict()
    can_next[0] = [2, 3, 4]
    can_next[1] = [4]
    can_next[2] = [0, 4, 5]
    can_next[3] = [0]
    can_next[4] = [3, 5]
    can_next[5] = [2]

    N = int(lin[0])
    R = int(lin[1])
    Y = int(lin[3])
    B = int(lin[5])

    if R > int(N/2):
        return "IMPOSSIBLE"
    if Y > int(N/2):
        return "IMPOSSIBLE"
    if B > int(N/2):
        return "IMPOSSIBLE"

    map = ['N', 'R', 'O', 'Y', 'G', 'B', 'V']


    index = 0
    ans_string = [""]*N

    lin2 = deepcopy(lin)

    for k in range(3):
        ind = which_index_max(lin2, [1, 3, 5])
        for z in range(int(lin[ind])):
            ans_string[index] = map[ind]
            index += 2
            index = index % N
            if ans_string[index] != "":
                index += 1
        lin2[ind] = -1

    return ''.join(ans_string)


if __name__ == '__main__':
    testcases = int(input())

    for nth_case in range(1, testcases + 1):
        N_lin = input().split(" ")

        print("Case #%i: %s" % (nth_case, solve(N_lin)))
