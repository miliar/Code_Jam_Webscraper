import sys


def pancakes(ps, k):
    return pancakes_rec(ps, 0, k)


def pancakes_rec(ps, index, k):
    if index == len(ps):
        return 0
    if ps[index] == "+":
        return pancakes_rec(ps, index+1, k)
    new_ps = flip(ps, index, k)
    if new_ps == -1:
        return "IMPOSSIBLE"
    return incr_result(pancakes_rec(new_ps, index+1, k))


def incr_result(res):
    if res == "IMPOSSIBLE":
        return res
    return int(res) + 1


def flip(ps, index, k):
    if index + k > len(ps):
        return -1
    part1 = ps[:index]
    part2 = flip_block(ps[index:index+k])
    part3 = ps[index+k:]
    return part1 + part2 + part3


def flip_block(block):
    new_block = ""
    for d in block:
        if d == "+":
            new_block += "-"
        else:
            new_block += "+"
    return new_block


sys.setrecursionlimit(10000)
t = int(raw_input())
for i in xrange(1, t + 1):
    input_str, input_k = [s for s in raw_input().split(" ")]
    result = pancakes(input_str, int(input_k))
    print "Case #{}: {}".format(i, result)
