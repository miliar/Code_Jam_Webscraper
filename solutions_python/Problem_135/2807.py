#!/usr/bin/env python


def task():
    a = int(raw_input()) - 1
    first = [raw_input().split(' ') for _ in range(4)]
    b = int(raw_input()) - 1
    second = [raw_input().split(' ') for _ in range(4)]

    result = set(first[a])
    result.intersection_update(set(second[b]))
    if len(result) == 1:
        return list(result)[0]
    elif len(result) == 0:
        return 'Volunteer cheated!'
    return 'Bad magician!'


def main():
    T = int(raw_input())
    for _ in xrange(T):
        print 'Case #%d: %s' % (_ + 1, task())


if __name__ == '__main__':
    main()
