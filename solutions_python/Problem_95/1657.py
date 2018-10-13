from optparse import OptionParser

#crypt => eng
LANG = dict([(' ', ' '), ('a', 'y'), ('b', 'h'), ('c', 'e'), ('d', 's'), ('e', 'o'), ('f', 'c'), ('g', 'v'), ('h', 'x'), ('i', 'd'), ('j', 'u'), ('k', 'i'), ('l', 'g'), ('m', 'l'), ('n', 'b'), ('o', 'k'), ('p', 'r'), ('q', 'z'),('r', 't'), ('s', 'n'), ('t', 'w'), ('u', 'j'), ('v', 'p'), ('w', 'f'), ('x', 'm'), ('y', 'a'), ('z', 'q')])

def translate(str):
    global LANG
    return "".join(LANG[c] for c in str)

def problem_A(filename):
    with open(filename, 'rU') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
    ntestcases = int(lines[0])
    for i in range(ntestcases):
        print "Case #%d: %s" % (i+1, translate(lines[i + 1]))





if __name__ == "__main__":
    parser = OptionParser()
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of arguments")
    problem_A(args[0])