import sys

def transform(char):
    d = {' ' : ' ',
         'a' : 'y',
         'b' : 'h',
         'c' : 'e',
         'd' : 's',
         'e' : 'o',
         'f' : 'c',
         'g' : 'v',
         'h' : 'x',
         'i' : 'd',
         'j' : 'u',
         'k' : 'i',
         'l' : 'g',
         'm' : 'l',
         'n' : 'b',
         'o' : 'k',
         'p' : 'r',
         'q' : 'z',
         'r' : 't',
         's' : 'n',
         't' : 'w',
         'u' : 'j',
         'v' : 'p',
         'w' : 'f',
         'x' : 'm',
         'y' : 'a',
         'z' : 'q' 
         }
    return d[char]

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    print "Case #%d: " % (case + 1),
    line = f.readline().strip()
    for char in line:
        sys.stdout.write(transform(char))
    print
