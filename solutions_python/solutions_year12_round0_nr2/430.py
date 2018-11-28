from __future__ import division
import sys
from contextlib import closing


def open_argv():
    return open(sys.argv[1])


def how_many(votes, surprising, max_vote):
    count = 0

    for vote in votes:
        vote -= max_vote
        if vote < 0:
            continue
        if vote / 2 >= max_vote - 1:
            count += 1
        elif (vote / 2 >= (max_vote - 2)) and surprising:
            surprising -= 1
            count += 1
    return count


def main():
    with closing(open_argv()) as f:
        n = int(f.readline())

        for index in range(n):
            line = map(int, f.readline().split())
            _, surprising, max_vote = line[:3]
            votes = line[3:]

            result = how_many(votes, surprising, max_vote)

            print 'Case #{0}: {1}'.format(index + 1, result)


if __name__ == '__main__':
    main()
