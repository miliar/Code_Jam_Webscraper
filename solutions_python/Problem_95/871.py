import sys, os

if len(sys.argv) > 1:
    f = open(sys.argv[1], 'r')
    fo = open(sys.argv[1] + '.out', 'w')

    map = {"e": "o", "j": "u", "p": "r", "m": "l", "y": "a", "s": "n",
           "l": "g", "c": "e", "k": "i", "d": "s", "x": "m", "v": "p",
           "n": "b", "r": "t", "i": "d", "b": "h", "t": "w", "a": "y",
           "h": "x", "w": "f", "f": "c", "o": "k", "u": "j", "g": "v",
           "q": "z", "z": "q", " ": " ", "\n": ""}
    cno = int(f.readline())
    print cno
    for c in range(1,cno+1):
        dec = ""
        line = f.readline()
        for i in line:
            dec = dec + map[i]
        if c != 1:
            fo.write("\n" + 'Case #'+str(c)+': ' + dec)
        else:
            fo.write('Case #'+str(c)+': ' + dec)
    f.close()
    fo.close()
