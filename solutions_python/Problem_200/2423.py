#!/usr/bin/python


def output(num, msg):
    print 'Case #%d: %s' % (num, msg)

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        n = map(int, list(raw_input()))
        while not is_tidy(n):
            for i in range(len(n) - 1):
                if n[i] > n[i+1]:
                    n[i] -= 1
                    for ii in range(i+1, len(n)):
                        n[ii] = 9
                    break
        output(t, int(''.join(map(str, n))))

def is_tidy(n):
    for i in range(len(n) - 1):
        if n[i] > n[i+1]:
            return False
    return True


if __name__ == '__main__':
    main()
