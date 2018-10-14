
FILENAME = "A-large.in"
OUTPUT = "op_pancake_large.txt"
def main():
    f = open(FILENAME, "r")
    o = open(OUTPUT, "w")

    testcases = int(f.readline())
    n = 1
    for i in f:
        inp = i.split()
        try:
            res = pancake(inp[0], int(inp[1]))
        except ValueError:
            res = "IMPOSSIBLE"
        o.write("Case #" + str(n) + ": " + str(res) + "\n")
        n += 1
    o.close()
    f.close()
    return


def turn(s):
    t = ""
    for ch in s:
        if ch == "+":
            t += "-"
        else:
            t += "+"
    return t


def pancake(pstring, K):
    # if all + return 0

    c = 0
    while True:

        l = len(pstring)

        if l * "+" == pstring:
            return c

        if l < K:
            raise ValueError

        if l == K:
            if l * "-" == pstring:
                c = c+1
                return c
            else:
                raise ValueError

        idx = pstring.index("-")

        if idx + K > l:
            raise ValueError

        if l > K:
            pstring = turn(pstring[idx:idx+K]) + pstring[idx+K:]
            c+=1

main()