#!/usr/bin/python2.7

def is_tidy(x):
    s = str(x)
    return all( int(i) <= int(j) for (i,j) in zip(s, s[1:]) )

def dirt_indeces(s):
    for index, (i,j) in enumerate(zip(s, s[1:])):
        if not int(i) <= int(j):
            yield index
    

class TidyAlrady(Exception):
    pass

def tidy_once(x):
    s = str(x)
    try:
        first_dirt_index = next(dirt_indeces(s))
    except StopIteration:
        raise TidyAlrady()

    tidyed = s[: first_dirt_index]
    tidyed += str( int(s[first_dirt_index]) - 1)
    tidyed += '9' * (len(s) - len(tidyed))
    return int(tidyed)


def make_tidy(x):
    try:
        for _ in str(x):
            x = tidy_once(x)
    except TidyAlrady:
        pass

    return x

if __name__ == '__main__':
    T = int(raw_input())
    for case in range(1, T+1):
        n = int(raw_input())
        print "Case #{}: {}".format(case, make_tidy(n))

