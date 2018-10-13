from Queue import PriorityQueue

def input_list(file_name):
    test = []
    with open(file_name, 'r') as reader:
        T = int(next(reader).strip())
        for ind in range(T):
            line = next(reader)
            strs = line.strip().split(' ')
            tu = (int(strs[0]), int(strs[1]))
            test.append(tu)
    reader.close()
    return test


def print_line(ind, max_s, min_s):
    return 'Case #{}: {} {}\n'.format(ind, max_s, min_s)


def last_space(N, K):
    avail_queue = PriorityQueue(maxsize=0)
    avail_queue.put((-N, N))
    for ind in range(K):

        current_max = avail_queue.get()[1]
        if current_max & 1:
            sub_max = (current_max - 1)/2
            sub_min = sub_max
        else:
            sub_max = current_max / 2
            sub_min = sub_max - 1

        if ind == K - 1:
            return sub_max, sub_min
        if sub_max > 0:
            avail_queue.put((-sub_max, sub_max))
        if sub_min > 0:
            avail_queue.put((-sub_min, sub_min))
    return 0, 0


if __name__ == '__main__':
    test_list = input_list('C-small-1-attempt1.in')
    f = open('C-small-1-attempt1.out', 'w')
    ind = 1
    for N, K in test_list:
        pair = last_space(N, K)
        f.write(print_line(ind, *pair))
        ind += 1
    f.close()
