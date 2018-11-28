# Q round 2012
# char map
d = {
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
    'r' : 't',
    's' : 'n',
    'q' : 'z',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'y' : 'a',
    'x' : 'm',
    'z' : 'q',
    ' ' : ' '
    }

data_in = open('./data/A-small-attempt2.in')
num_cases = int(data_in.readline())

for i in range(num_cases):
    case = data_in.readline().strip('\n')
    decodedCase = ''
    
    for char in case:
        decodedCase = decodedCase + d[char]
        
    print 'Case #%d: %s' % (i+1, decodedCase)
