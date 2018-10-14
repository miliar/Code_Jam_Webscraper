#!/usr/bin/python3


def main():
    input()
    tcase = 0
    while True:
        tcase += 1
        try:
            s = input()
        except EOFError:
            return
        ns = [int(x) for x in s.split()[1]]
        added = 0
        standing = 0
        for (i, n) in enumerate(ns):
            if standing >= i:
                standing += n
            else:
                added += i - standing
                standing += i - standing
                standing += n
        print('Case #{}: {}'.format(tcase, added))

if __name__ == '__main__':
    main()
