import sys

def main(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    
    d = {}
    d['a'] = 'y'
    d['b'] = 'h'
    d['c'] = 'e'
    d['d'] = 's'
    d['e'] = 'o'
    d['f'] = 'c'
    d['g'] = 'v'
    d['h'] = 'x'
    d['i'] = 'd'
    d['j'] = 'u'
    d['k'] = 'i'
    d['l'] = 'g'
    d['m'] = 'l'
    d['n'] = 'b'
    d['o'] = 'k'
    d['p'] = 'r'
    d['q'] = 'z'
    d['r'] = 't'
    d['s'] = 'n'
    d['t'] = 'w'
    d['u'] = 'j'
    d['v'] = 'p'
    d['w'] = 'f'
    d['x'] = 'm'
    d['y'] = 'a'
    d['z'] = 'q'
    
    case = 1
    
    for line in lines[1:]:
        answer = ''
        for letter in line:
            if letter != '\n':
                if letter == ' ':
                    answer += ' '
                else: 
                    answer += d[letter]
                
        print "Case #%d: %s" % (case, answer)
        case += 1
    
if __name__ == '__main__':
    main(sys.argv[1])