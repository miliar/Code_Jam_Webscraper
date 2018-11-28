import sys

map = {"a": "y",
       "b": "h",
       "c": "e",
       "d": "s",
       "e": "o",
       "f": "c",
       "g": "v",
       "h": "x",
       "i": "d",
       "j": "u",
       "k": "i",
       "l": "g",
       "m": "l",
       "n": "b",
       "o": "k",
       "p": "r",
       "q": "z",
       "r": "t",
       "s": "n",
       "t": "w",
       "u": "j",
       "v": "p",
       "w": "f",
       "x": "m",
       "y": "a",
       "z": "q"}


def main():
    inp = open(sys.argv[1], "r")
    out = open(sys.argv[2], "w")

    T = int(inp.readline())

    if not T:
        return

    for i in xrange(T):
        GSTRING = inp.readline().strip()
        NSTRING = "Case #" + str(i + 1) + ": "
        for c in GSTRING:
            if c == " ":
                NSTRING += " "
            else:
                NSTRING += map[c]
        out.write(NSTRING)
        if i < T -1:
            out.write("\n")

if __name__ == "__main__":
    main()
