from math import sqrt


def grow(text, start, end):
    "Start with a 0- or 1- length palindrome; try to grow a bigger one."
    while (start > 0 and end < len(text)
            and text[start - 1].upper() == text[end].upper()):
        start -= 1
        end += 1
    return (start, end)


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longes palindrome."
    if text == '':
        return (0, 0)

    def length(slice):
        a, b = slice
        return b - a

    candidates = [grow(text, start, end)
                      for start in xrange(len(text))
                      for end in (start, start + 1)]

    return max(candidates, key=length)


def gen_square():
    i = 1
    while True:
        yield i, i ** 2
        i += 1

g = gen_square()


def fair_and_square(a, b):
    L = longest_subpalindrome_slice
    g = gen_square()
    x, x2 = g.next()
    string2 = str(x2)
    string = str(x)
    c = 0
    while x2 <= b:
        if a <= x2:
            s1, e1 = L(string)
            s2, e2 = L(string2)
            if (e2 - s2) == len(string2) and (e1 - s1) == len(string):
                c += 1
        x, x2 = g.next()
        string2 = str(x2)
        string = str(x)
    return c


def solve():
    fin = open("C-small-attempt0.in", "r")
    fout = open("result.txt", "w")
    num_tests = int(fin.readline())

    for i in xrange(num_tests):
        line = fin.readline()
        a, b = map(int, line.split())

        c = fair_and_square(a, b)
        fout.write("Case #%d: %d\n" % (i+1, c))
    fin.close()
    fout.close()

solve()
