import sys

char_map = {
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
    'z' : 'q', 
    ' ' : ' ',
}

if __name__ == '__main__':
    filename = sys.argv[1]   
    f = open(filename)
    cases = int(f.readline().strip())
    for n in xrange(1,cases+1):
        result = ''
        line = f.readline().strip()
        for c in line:
            result += char_map[c] 
        print 'Case #%d:'%n, result

