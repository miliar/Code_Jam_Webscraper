import math


def _assign_a_stall(arr1):
    max_space_between_stalls = max(arr1)
    ls, rs = _get_ls_and_rs(max_space_between_stalls)
    arr1.remove(max_space_between_stalls)
    arr1.append(ls)
    arr1.append(rs)


def _get_ls_and_rs(max_space_between_stalls):
    location = math.ceil(max_space_between_stalls / 2)
    ls = location - 1
    rs = max_space_between_stalls - location
    return ls, rs


def run_code(stalls, people):
    arr1 = [stalls]
    for person in range(0, people-1):
        _assign_a_stall(arr1)
    ls, rs = _get_ls_and_rs(max(arr1))
    return max(ls, rs), min(ls, rs)


t = int(input())
for i in range(1, t + 1):
    stalls, people = [int(s) for s in input().split(" ")]
    n1, n2 = run_code(stalls, people)
    print("Case #{}: {} {}".format(i, n1, n2))