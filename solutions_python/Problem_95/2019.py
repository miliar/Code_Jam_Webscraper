d = {\
    'y':'a', 'n':'b', 'f':'c', 'i':'d',\
    'c':'e', 'w':'f', 'l':'g', 'b':'h',\
    'k':'i', 'u':'j', 'o':'k', 'm':'l',\
    'x':'m', 's':'n', 'e':'o', 'v':'p',\
    'z':'q', 'p':'r', 'd':'s', 'r':'t',\
    'j':'u', 'g':'v', 't':'w', 'h':'x',\
    'a':'y', 'q':'z', ' ':' '\
    }
#Missing 'q' and 'z'

def googerase(s):
    toRet = ''
    for c in s:
        toRet = toRet + (d[c])
    if 'q' in s:
        print('WARNING! ' + toRet)
    elif 'z' in s:
        print('WARNING! ' + toRet)
    return toRet

def solve_func(infile, outfile):
    #read the number of cases
    cases = int(str(infile.readline()[:-1], 'utf8'))
    #for each case
    for i in range(cases):
        #convert the string
        msg = googerase(str(infile.readline()[:-1], 'utf8'))
        msg = 'Case #%d: %s\n' % (i+1, msg)
        outfile.write(bytes(msg, 'utf8'))


if __name__ == '__main__':
    infile  = open('in', 'rb')
    outfile = open('out', 'wb')
    try:
        solve_func(infile, outfile)
    finally:
        infile.close()
        outfile.close()
