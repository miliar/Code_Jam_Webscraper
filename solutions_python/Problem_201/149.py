import sys
import bisect


def answer(n, k):
    interval_lengths = [n]
    for i in range(k):
        last = interval_lengths[-1] - 1
        #if last == 0:
        #    print "Fuck!"
        del interval_lengths[-1]
        min_dist, max_dist = int(last/2), int((last+1)/2)
        bisect.insort(interval_lengths, min_dist)
        bisect.insort(interval_lengths, max_dist)

    return ' '.join(map(str, [max_dist, min_dist]))


def answer2(n, k):
    interval_lengths = [n]
    counter = 1
    while True:
        new_interval_lengths = []
        for num in interval_lengths:
            min_dist, max_dist = int((num-1)/2), int(num/2)
            new_interval_lengths.extend([min_dist, max_dist])
            if counter == k:
                return ' '.join(map(str, [max_dist, min_dist]))
            counter += 1
        interval_lengths = sorted(new_interval_lengths, reverse=True)
    assert False


def answer3(n, k):
    binary_k = "{0:#b}".format(k)[2:]
    level = len(binary_k) - 1
    if level == 0:
        index_in_level = 0
    else:
        index_in_level = int(binary_k[1:], 2)
    sum_in_level = n - (2 ** level - 1)
    min_value_in_level = int(sum_in_level / (2 ** level))
    residue = sum_in_level - (min_value_in_level * (2 ** level))
    interval_length = min_value_in_level + int(index_in_level < residue)
    min_dist, max_dist = int((interval_length - 1) / 2), int(interval_length / 2)
    return ' '.join(map(str, [max_dist, min_dist]))



if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        queries.append(map(int, sys.stdin.next().split()))
    for i, q in enumerate(queries):
        #if answer3(*q) != answer2(*q):
        #    raise ValueError('Wrong answer on {}'.format(q))
        print "".join(["Case #", str(i+1), ": ", str(answer3(*q))])
