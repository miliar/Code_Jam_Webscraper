#! /usr/bin/env python

sub = dict()

sub['a'] = 'y'
sub['b'] = 'n'
sub['c'] = 'f'
sub['d'] = 'i'
sub['e'] = 'c'
sub['f'] = 'w'
sub['g'] = 'l'
sub['h'] = 'b'
sub['i'] = 'k'
sub['j'] = 'u'
sub['k'] = 'o'
sub['l'] = 'm'
sub['m'] = 'x'
sub['n'] = 's'
sub['o'] = 'e'
sub['p'] = 'v'
sub['q'] = 'z'
sub['r'] = 'p'
sub['s'] = 'd'
sub['t'] = 'r'
sub['u'] = 'j'
sub['v'] = 'g'
sub['w'] = 't'
sub['x'] = 'h'
sub['y'] = 'a'
sub['z'] = 'q'




print len(set(sub.values()))
t = dict()
for elem in sub:
    t[sub[elem]] = elem 

def translate(lang, s):
    out = ''
    for ch in s:
        if ch == ' ':
            out += ' '
        else:
            out += lang[ch]

    return out


with open('a.txt', 'r') as f:
    discard = True
    count = 1
    for line in f:
        if discard:
            discard = False
            continue

        print "Case #%s: %s" % (count, translate(t, line.rstrip()))
        count += 1
