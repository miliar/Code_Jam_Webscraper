import sys


def main():
    T = int(raw_input().strip())
    count = 1
    for _ in xrange(T):
        N = int(raw_input().strip())
        while 1:
            str_N = str(N)
            if len(str_N) == 1:
                break
            i = 0
            len_N = len(str_N)
            while i < len_N - 1 and str_N[i] <= str_N[i + 1]:
                i += 1
            if i == len_N - 1:
                break
            else:
                N -= 1
        print 'Case #' + str(count) + ': ' + str(N)
        count += 1

if __name__ == '__main__':
    main()
