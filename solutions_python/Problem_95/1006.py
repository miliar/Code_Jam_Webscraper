o = open("q1.output", 'r+')
cnt = 1

with open("q1.input") as f:
    while True:
        c = f.read(1)
        if not c:
            print "Enod of file"
            break
        print "Read a character:", c

        if c == "y":
            c = "a"
        elif c == "n":
            c = "b"
        elif c == "f":
            c = "c"
        elif c == "i":
            c = "d"
        elif c == "c":
            c = "e"
        elif c == "w":
            c = "f"
        elif c == "l":
            c = "g"
        elif c == "b":
            c = "h"
        elif c == "k":
            c = "i"
        elif c == "u":
            c = "j"
        elif c == "o":
            c = "k"
        elif c == "m":
            c = "l"
        elif c == "x":
            c = "m"
        elif c == "s":
            c = "n"
        elif c == "e":
            c = "o"
        elif c == "v":
            c = "p"
        elif c == "z":
            c = "q"
        elif c == "p":
            c = "r"
        elif c == "d":
            c = "s"
        elif c == "r":
            c = "t"
        elif c == "j":
            c = "u"
        elif c == "g":
            c = "v"
        elif c == "t":
            c = "w"
        elif c == "h":
            c = "x"
        elif c == "a":
            c = "y"
        elif c == "q":
            c = "z"

        print "Replaced with a character:", c

        o.write(c)

        if c == "\n":
            o.write('Case #')
            o.write(str(cnt))
            o.write(': ')
            cnt += 1


o.close()
