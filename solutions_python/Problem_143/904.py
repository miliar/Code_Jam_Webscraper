def main():
    f_in = open('B-small-attempt0.in', 'r')
    f_out = open('B-small-attempt0.out', 'w')
    cases = int(f_in.readline())
    for case in xrange(cases):
        a, b, k = [int(s) for s in f_in.readline().split()]
        win_count = 0
        for a_num in xrange(a):
            for b_num in xrange(b):
                if a_num & b_num < k:
                    win_count += 1
        f_out.write('Case #{}: {}\n'.format(case + 1, win_count))
    f_in.close()
    f_out.close()


if __name__ == '__main__':
    main()