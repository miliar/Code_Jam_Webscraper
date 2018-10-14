#/usr/bin/python
# -*- coding: utf-8 -*-

import re


def win_symbol(symb, desc):
    without_separators = "".join(desc)
    # diag 1
    if re.match("^[%sT](.{4}[%sT]){3}$" % (symb, symb), without_separators):
        return True
    # diag 2
    if re.match("^.{3}[%sT](.{2}[%sT]){3}.{3}$" % (symb, symb), without_separators):
        return True

    # column
    if re.match("^.{0,3}[%sT](.{3}[%sT]){3}.{0,3}$" % (symb, symb), without_separators):
        return True

    with_separators = "|" + "|".join(desc) + "|"
    # line
    if re.match("^.*\|[%sT]{4}\|.*$" % symb, with_separators):
        return True    
    return False

if __name__ == "__main__":
    inp = open("tick_tack.inp", "r")
    out = open("tick_tack.out", "w")
    tests = int(inp.readline())
    for test in xrange(tests):
        
        desc = []
        desc.append(inp.readline().strip())
        desc.append(inp.readline().strip())
        desc.append(inp.readline().strip())
        desc.append(inp.readline().strip())
        
        inp.readline()

        win_x = win_symbol('X', desc)
        win_o = win_symbol('O', desc)
        not_completed = "." in ("".join(desc))

        if win_x:
            res = "X won"
        elif win_o:
            res = "O won"
        elif not_completed:
            res = "Game has not completed"
        else:
            res = "Draw"

        out.write("Case #%d: %s\n" % (test + 1, res))
    out.close()