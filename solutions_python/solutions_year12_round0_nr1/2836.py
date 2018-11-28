infile = open('/A-small-attempt1.in', 'r').read()
outfile = file('/A-small-attempt1.out', 'w')

lines = infile.split('\n')
lines.pop(0)

dictionary = {  ' ':' ',
                'y':'a',
                'n':'b',
                'f':'c',
                'i':'d',
                'c':'e',
                'w':'f',
                'l':'g',
                'b':'h',
                'k':'i',
                'u':'j',
                'o':'k',
                'm':'l',
                'x':'m',
                's':'n',
                'e':'o',
                'v':'p',
                'z':'q',
                'p':'r',
                'd':'s',
                'r':'t',
                'j':'u',
                'g':'v',
                't':'w',
                'h':'x',
                'a':'y',
                'q':'z'
                }

for line in range(len(lines)):
    outstring = ''
    letterlist = [char for char in lines[line]]
    if letterlist==[]: break
    for letter in range(len(letterlist)):
        letterlist[letter] = dictionary[letterlist[letter]]
        outstring = outstring + letterlist[letter]
    print 'Case #' + str(line + 1) + ': ' + outstring
    outfile.write('Case #' + str(line + 1) + ': ' + outstring + '\n')
outfile.close()
