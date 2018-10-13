def max_number_of_googlers(n, s, p, sums):
    sufficient_sum_number = 0
    suprising_sum_number = 0
    for k in sums:
        d = 3 * p - k
        if d > 2 and d <= 4 and k >= p:
            suprising_sum_number += 1
        if d <= 2:
            sufficient_sum_number += 1
    return sufficient_sum_number + min(suprising_sum_number, s)

if __name__ == '__main__':
    t = input()
    for i in xrange(t):
        line = raw_input()
        numbers = map(int, line.split())
        n = numbers[0]
        s = numbers[1]
        p = numbers[2]
        sums = numbers[3:]
        print 'Case #{}: {}'.format(i + 1, max_number_of_googlers(n, s, p, sums))

