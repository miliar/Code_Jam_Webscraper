mapping = {
    'y' : 'a',
    'n' : 'b',
    'f' : 'c',
    'i' : 'd',
    'c' : 'e',
    'w' : 'f',
    'l' : 'g',
    'b' : 'h',
    'k' : 'i',
    'u' : 'j',
    'o' : 'k',
    'm' : 'l',
    'x' : 'm',
    's' : 'n',
    'e' : 'o',
    'v' : 'p',
    'z' : 'q',
    'p' : 'r',
    'd' : 's',
    'r' : 't',
    'j' : 'u',
    'g' : 'v',
    't' : 'w',
    'h' : 'x',
    'a' : 'y',
    'q' : 'z',
    ' ' : ' '
}

T = int(raw_input())
for t in range(0,T):
    inp = raw_input()
    result = ''
    for index in range(0, len(inp)):
        result = result + mapping[inp[index]]
    print "Case #%d: %s" %(t + 1, result)
