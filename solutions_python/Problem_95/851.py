#!/usr/bin python

import sys

input = sys.stdin


def data():
    input.readline()
    for l in input:
        yield l.strip()


def results(f=None):
    for i, l in enumerate(data()):
        print "Case #" + str(i + 1) + ":", f(l)


if __name__ == "__main__":
    samples = ["ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq",
               "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz"]
    m = {}
    for i, letter in enumerate(samples[0]):
        m[letter] = samples[1][i]

    f = lambda l: "".join([m[x] for x in l])

    results(f)
