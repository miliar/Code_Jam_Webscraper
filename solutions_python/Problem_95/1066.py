# -*- coding: cp932 -*-

num_in = input()
num_out = 1

while 0 < num_in :
    s = raw_input()

    table = map(chr,xrange(0,256))
    table[ord("a")] = "y"
    table[ord("b")] = "h"
    table[ord("c")] = "e"
    table[ord("d")] = "s"
    table[ord("e")] = "o"
    table[ord("f")] = "c"
    table[ord("g")] = "v"
    table[ord("h")] = "x"
    table[ord("i")] = "d"
    table[ord("j")] = "u"
    table[ord("k")] = "i"
    table[ord("l")] = "g"
    table[ord("m")] = "l"
    table[ord("n")] = "b"
    table[ord("o")] = "k"
    table[ord("p")] = "r"
    table[ord("q")] = "z"
    table[ord("r")] = "t"
    table[ord("s")] = "n"
    table[ord("t")] = "w"
    table[ord("u")] = "j"
    table[ord("v")] = "p"
    table[ord("w")] = "f"
    table[ord("x")] = "m"
    table[ord("y")] = "a"
    table[ord("z")] = "q"


    out = s.translate("".join(table))

    print "Case #" + str(num_out) + ": " + out
    num_out += 1
    num_in -= 1
