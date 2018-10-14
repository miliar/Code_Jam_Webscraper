import sys
import string

I = " abcdefghijklmnopqrstuvwxyz"
O = " ynficwlbkuomxsevzpdrjgthaq"

def translate(googlerese):
    result = ""
    for char in googlerese:
        if char != '\n':
            result += I[O.index(char)]
    return result

def run():
    lines = sys.stdin.readlines()
    line_num = 1
    for line in lines[1:]:
        print "Case #%s: %s" % (line_num, translate(line))
        line_num += 1

run()
