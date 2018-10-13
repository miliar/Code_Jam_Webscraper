import sys


def handle_test_case(f, i):
    content = f.readline()
    max_shyness, level_str = content.split(' ')
    level_arr = [int(c) for c in level_str.strip()]
    diff_arr = list()

    diff_arr.append(level_arr[0])
    needed = 0
    for j in xrange(1, int(max_shyness) + 1):
        diff_arr.append(diff_arr[j - 1])
        if diff_arr[j] < j:
            to_add = j - diff_arr[j - 1]
            needed += to_add
            diff_arr[j] += to_add
        diff_arr[j] += level_arr[j]

    print "Case #{}: {}".format(i + 1, needed)


if __name__ == "__main__":
    f = open(sys.argv[1], 'rb')
    num_test_cases = int(f.readline())
    for i in xrange(num_test_cases):
        handle_test_case(f, i)