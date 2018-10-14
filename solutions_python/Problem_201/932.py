from sortedcontainers import SortedDict


def replace_list_element_with_pair(elements, index_of_element, a, b):
    elements[index_of_element : index_of_element + 1] = a, b
    return elements


def is_power_of_2(n):
    return ((n & (n - 1)) == 0) and n != 0


def naivesolve(n, k):
    space_pattern = [n]
    while k > 0:
        max_space = max(space_pattern)
        lhalf = (max_space - 1)/2
        rhalf = max_space/2
        assert(rhalf >= lhalf)

        if k == 1:
            return rhalf, lhalf

        index_of_max_space = space_pattern.index(max_space)
        replace_list_element_with_pair(space_pattern, index_of_max_space, lhalf, rhalf)

        k -= 1

    print "Shouldn't happen"


def solve(n, k):
    spaces = SortedDict({n: 1})
    while True:
        space_size, repeat = spaces.popitem()
        lsize = (space_size - 1) / 2
        rsize = space_size / 2
        if k <= repeat:
            return rsize, lsize
        if lsize in spaces:
            spaces[lsize] += repeat
        else:
            spaces[lsize] = repeat
        if rsize in spaces:
            spaces[rsize] += repeat
        else:
            spaces[rsize] = repeat

        k -= repeat

t = int(raw_input())

for i in xrange(1, t+1):
    n, k = map(int, raw_input().split())
    print "Case #{}: {} {}".format(i, *solve(n, k))
