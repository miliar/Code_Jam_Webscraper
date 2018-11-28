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

    for j in xrange(T):
        count = 0
        possible_count = 0
        IN_STRING = inp.readline().strip()
        OUT_STRING = "Case #" + str(j + 1) + ": "
        arr = IN_STRING.split(" ")
        N = int(arr[0])
        S = int(arr[1])
        p = int(arr[2])
        for i in xrange(3, len(arr)):
            val = int(arr[i])
            if val > 3*(p - 1):
                count += 1
            elif p >= 2 and val > 3 * (p - 2):
                if possible_count < S and val % 3 != 1:
                    possible_count += 1
        out.write(OUT_STRING + str(count + possible_count))
        if j < T -1:
            out.write("\n")

if __name__ == "__main__":
    main()
