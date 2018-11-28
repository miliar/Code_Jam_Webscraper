import sys
from string import maketrans

sheet = {' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'q',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'z'}

f = ' acbedgfihkjmlonqpsrutwvyxz'
t = ' yehosvcdxiulgkbzrntjwfpamq'
 
 
if __name__ == '__main__':
    fileName = sys.argv[1]
    trantable = maketrans(f,t)
    with open(fileName + '.in') as data:
        T = int(data.readline().strip())
        for i in range(T):
            s = data.readline().strip()
            print "Case #%s: %s" % (i+1, s.translate(trantable))
