# Marius Damarackas (m.damarackas@gmail.com)
# Google CodeJam, Qualification Round 2009, Welcome to Code Jam

welcome = "welcome to code jam"
string = ""
memoize = { }

def count(pos, wi):
    if (pos, wi) in memoize:
        return memoize[(pos, wi)]
    total = sum(count(i, wi - 1)
                for i in range(pos) if string[i] == welcome[wi - 1])
    memoize[(pos, wi)] = total % 10000
    return total % 10000

def solve(paragraph):
    global string, memoize
    string = paragraph
    memoize = { }
    for i in range(len(welcome)):
        memoize[(0, i + 1)] = 0
    for i in range(len(string)):
        memoize[(i + 1, 1)] = string[:(i + 1)].count("w")
    return str(count(len(string), len(welcome))).rjust(4, "0")

def main():
    file = open("input.in")
    tests = int(file.readline().strip())
    for case in range(1, tests + 1):
        paragraph = file.readline().strip()
        print("Case #", case, ": ", solve(paragraph), sep="")

if __name__ == "__main__":
    main()
