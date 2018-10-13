import sys
import re

if __name__ == "__main__":

    googlerese = {
        'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o',
        'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u',
        'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k',
        'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w',
        'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a',
        'z':'q', ' ':' ', '\n':''
        }

    maxCase = int(sys.stdin.readline())
    for line in range(1, maxCase+1):
        text = sys.stdin.readline()
        newword = ""
        for i in range(0, len(text)):
            newword += googlerese[text[i]]
        print "Case #%d: %s" % (line, newword)
