import string
import sys

rows = int(int(sys.stdin.readline()))

for i in range(rows):
    text = str(sys.stdin.readline())
    out = list(text)
    for l in range(len(out)):
        try:
            out[l] = {
              'a': "y",#
              'b': "h",#???
              'c': "e",#
              'd': "s",#
              'e': "o",#
              'f': "c",#
              'g': "v",#
              'h': "x",
              'i': "d",#
              'j': "u",#
              'k': "i",#
              'l': "g",#
              'm': "l",#
              'n': "b",#
              'o': "k",#
              'p': "r",#
              'q': "z",#
              'r': "t",#
              's': "n",#
              't': "w",#
              'u': "j",#
              'v': "p",#
              'w': "f",#
              'x': "m",#
              'y': "a",#
              'z': "q",
              ' ': " ",
              '\r': "",
              '\n': ""
            }[out[l]]
        except KeyError:
            out[l] = out[l]
    print string.join(["Case #", str(i+1), ": ", string.join(out, "")], "")