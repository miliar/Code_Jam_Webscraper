

def main():
    langhash = { 'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',#,
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'x': 'm',
    'z': 'q',#
    'k': 'i',
    'w': 'f',
    'y': 'a',
    ' ': ' '}
    f = open("A-small-attempt1.in")
    w = open("small.out", "w")
    line = f.readline()
    t = int(line.rstrip())
    for x in range(t):
        line = f.readline().rstrip()
        translated = ""
        for c in line:
            translated += langhash[c]
        print "Case #%d: %s" % (x+1, translated)
        
if __name__ == "__main__":
    main()