def solve(text):

    google_dict = {
            "a": "y",
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
            "z": "q",
            " ": " ",
            "\n": "",
            }

    return ''.join(google_dict.get(k) for k in text)

if __name__ == "__main__":

    f = open("inputs/1.txt", "r")
    T = ((int) (f.readline()))

    for x in xrange(T):
        print "Case #" + str(x + 1) + ": " + solve(f.readline())