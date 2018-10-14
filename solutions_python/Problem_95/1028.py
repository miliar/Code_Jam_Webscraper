# solution for https://code.google.com/codejam/contest/1460488/dashboard#s=p0
import sys


dictionary= {'a': 'y',
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
             'q': 'z',
             'r': 't',
             's': 'n',
             't': 'w',
             'u': 'j',
             'v': 'p',
             'w': 'f',
             'x': 'm',
             'y': 'a',
             'z': 'q',
            }
             
             
def solve(str):
    #init
    res = ''
    for c in str:
        res += dictionary[c] if c != ' ' else ' '
    return res
    
filename = sys.argv[1] #get filename from arguments
f_in = open(filename,'r')
output = filename.split('.in')[0] + '.out' # generate output filename
f_out = open(output,'w')
n = 0
cases = f_in.readline() #  number of testcases
for n in range(int(cases)):
    str = f_in.readline().rstrip()
    # for each test case do the convertion
    f_out.write('Case #%d: %s\n' %((n+1), solve(str)))