#! /usr/bin/python2.6
# coding: utf-8

m = dict(
    zip(
        'abcdefghijklmnopqrstuvwxyz ',
        'yhesocvxduiglbkrztnwjpfmaq '
        )
    )
for t in range(1, input() + 1):
    g = raw_input()
    print 'Case #%d:' % t,''.join(m[c] for c in g)
