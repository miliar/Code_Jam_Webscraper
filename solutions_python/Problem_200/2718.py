
FILENAME = "B-small-attempt0.in"
OUTPUT = "output.txt"

def main():
    f = open(FILENAME, "r")
    o = open(OUTPUT, "w")

    testcases = int(f.readline())
    n = 1
    for i in f:
        res = get_last_tidy(int(i))
        o.write("Case #" + str(n) + ": " + str(res) + "\n")
        n = n+1
    o.close()
    f.close()
    return

def get_last_tidy(inp):
    c = inp
    while not is_tidy(c):
        c = c-1
    return c

def is_tidy(inp):
    t = str(inp)
    last = -1
    for i in t:
        if int(i) < last:
            return False
        last = int(i)
    return True

main()