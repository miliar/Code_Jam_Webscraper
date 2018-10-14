import numpy as np


def tidify(n):
    numbers= [int(i) for i in str(n)]
    N = len(numbers)
    # edge case
    if N ==1:
        return str(n)


    curr, curr_pos = numbers[-1], N - 1

    while 0 < curr_pos:
        for i in xrange(curr_pos, -1, -1):
            if  curr < numbers[i]:
                for j in xrange(i+1, N):
                    numbers[j] = 9
                numbers[i] -= 1
                break
        curr_pos -= 1
        curr = numbers[curr_pos]
    for j, d in enumerate(numbers):
        if d != 0:
            break
    return ''.join([str(i) for i in numbers[j:]])


if __name__ == "__main__":
    t = int(raw_input())
    for idx in xrange(1, t + 1):
        n = int(raw_input())
        print "Case #{}: {}".format(idx, tidify(n))
