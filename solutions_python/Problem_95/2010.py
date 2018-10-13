#! /usr/bin/env python
import sys

# $ irb
# >> a='ejp mysljylc kd kxveddknmc re jsicpdrysi
# '> rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# '> de kr kd eoya kw aej tysr re ujdr lkgc jv
# '> '
#  => "ejp mysljylc kd kxveddknmc re jsicpdrysi\nrbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\nde kr kd eoya kw aej tysr re ujdr lkgc jv\n"
# >> b='Case #1: our language is impossible to understand
# '> Case #2: there are twenty six factorial possibilities
# '> Case #3: so it is okay if you want to just give up
# '> '
#  => "Case #1: our language is impossible to understand\nCase #2: there are twenty six factorial possibilities\nCase #3: so it is okay if you want to just give up\n"
# >> b.gsub! /Case #.: /, ""
#  => "our language is impossible to understand\nthere are twenty six factorial possibilities\nso it is okay if you want to just give up\n"
# >> a.chars.zip b.chars
#  => [["e", "o"], ["j", "u"], ["p", "r"], [" ", " "], ["m", "l"], ["y", "a"], ["s", "n"], ["l", "g"], ["j", "u"], ["y", "a"], ["l", "g"], ["c", "e"], [" ", " "], ["k", "i"], ["d", "s"], [" ", " "], ["k", "i"], ["x", "m"], ["v", "p"], ["e", "o"], ["d", "s"], ["d", "s"], ["k", "i"], ["n", "b"], ["m", "l"], ["c", "e"], [" ", " "], ["r", "t"], ["e", "o"], [" ", " "], ["j", "u"], ["s", "n"], ["i", "d"], ["c", "e"], ["p", "r"], ["d", "s"], ["r", "t"], ["y", "a"], ["s", "n"], ["i", "d"], ["\n", "\n"], ["r", "t"], ["b", "h"], ["c", "e"], ["p", "r"], ["c", "e"], [" ", " "], ["y", "a"], ["p", "r"], ["c", "e"], [" ", " "], ["r", "t"], ["t", "w"], ["c", "e"], ["s", "n"], ["r", "t"], ["a", "y"], [" ", " "], ["d", "s"], ["k", "i"], ["h", "x"], [" ", " "], ["w", "f"], ["y", "a"], ["f", "c"], ["r", "t"], ["e", "o"], ["p", "r"], ["k", "i"], ["y", "a"], ["m", "l"], [" ", " "], ["v", "p"], ["e", "o"], ["d", "s"], ["d", "s"], ["k", "i"], ["n", "b"], ["k", "i"], ["m", "l"], ["k", "i"], ["r", "t"], ["k", "i"], ["c", "e"], ["d", "s"], ["\n", "\n"], ["d", "s"], ["e", "o"], [" ", " "], ["k", "i"], ["r", "t"], [" ", " "], ["k", "i"], ["d", "s"], [" ", " "], ["e", "o"], ["o", "k"], ["y", "a"], ["a", "y"], [" ", " "], ["k", "i"], ["w", "f"], [" ", " "], ["a", "y"], ["e", "o"], ["j", "u"], [" ", " "], ["t", "w"], ["y", "a"], ["s", "n"], ["r", "t"], [" ", " "], ["r", "t"], ["e", "o"], [" ", " "], ["u", "j"], ["j", "u"], ["d", "s"], ["r", "t"], [" ", " "], ["l", "g"], ["k", "i"], ["g", "v"], ["c", "e"], [" ", " "], ["j", "u"], ["v", "p"], ["\n", "\n"]]
# >> Hash[*_.flatten]
#  => {"e"=>"o", "j"=>"u", "p"=>"r", " "=>" ", "m"=>"l", "y"=>"a", "s"=>"n", "l"=>"g", "c"=>"e", "k"=>"i", "d"=>"s", "x"=>"m", "v"=>"p", "n"=>"b", "r"=>"t", "i"=>"d", "\n"=>"\n", "b"=>"h", "t"=>"w", "a"=>"y", "h"=>"x", "w"=>"f", "f"=>"c", "o"=>"k", "u"=>"j", "g"=>"v"}
# >> MAP=_

MAP = {"e": "o", "j": "u", "p": "r", " ": " ", "m": "l", "y": "a", "s": "n", "l": "g", "c": "e", "k": "i", "d": "s", "x": "m", "v": "p", "n": "b", "r": "t", "i": "d", "\n": "\n", "b": "h", "t": "w", "a": "y", "h": "x", "w": "f", "f": "c", "o": "k", "u": "j", "g": "v"}
# also...
MAP['z'] = 'q'
MAP['q'] = 'z'


def main():
    n = int(raw_input())
    for i in xrange(1, n + 1):
        print 'Case #%d:' % i,
        print ''.join(MAP[c] for c in raw_input())


if __name__ == '__main__':
    sys.exit(main())
