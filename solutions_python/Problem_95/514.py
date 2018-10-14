import itertools

trans = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v',
         'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g',
         'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j',
         't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

def decipher(string):
    return "".join([trans[s] for s in string])

def solve(path):
    outpath = path.replace("in", "out")

    with open(path) as fin:
        with open(outpath, "w") as fout:
            num_cases = int(fin.readline())

            for n in range(num_cases):
                sol = decipher(fin.readline().strip())
                fout.write("Case #%i: %s\n" % (n+1, sol))
                print "Case #%i: %s" % (n+1, sol)