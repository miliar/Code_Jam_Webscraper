
infile = open('A-small-attempt0.in', 'r')
content = infile.readlines()
infile.close()

decode = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v',\
          'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b',\
          'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j',\
          'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}

outfile = open('problemAout.txt', 'w')
cleanString = ''

for i in range(1, eval(content[0]) + 1):
    caseString = "Case #" + str(i) + ": "
    outfile.write(caseString)
    for j in range(len(content[i])):
        if content[i][j] == 'a':
            cleanString += decode.get('a')
        if content[i][j] == 'b':
            cleanString += decode.get('b')
        if content[i][j] == 'c':
            cleanString += decode.get('c')
        if content[i][j] == 'd':
            cleanString += decode.get('d')
        if content[i][j] == 'e':
            cleanString += decode.get('e')
        if content[i][j] == 'f':
            cleanString += decode.get('f')
        if content[i][j] == 'g':
            cleanString += decode.get('g')
        if content[i][j] == 'h':
            cleanString += decode.get('h')
        if content[i][j] == 'i':
            cleanString += decode.get('i')
        if content[i][j] == 'j':
            cleanString += decode.get('j')
        if content[i][j] == 'k':
            cleanString += decode.get('k')
        if content[i][j] == 'l':
            cleanString += decode.get('l')
        if content[i][j] == 'm':
            cleanString += decode.get('m')
        if content[i][j] == 'n':
            cleanString += decode.get('n')
        if content[i][j] == 'o':
            cleanString += decode.get('o')
        if content[i][j] == 'p':
            cleanString += decode.get('p')
        if content[i][j] == 'q':
            cleanString += decode.get('q')
        if content[i][j] == 'r':
            cleanString += decode.get('r')
        if content[i][j] == 's':
            cleanString += decode.get('s')
        if content[i][j] == 't':
            cleanString += decode.get('t')
        if content[i][j] == 'u':
            cleanString += decode.get('u')
        if content[i][j] == 'v':
            cleanString += decode.get('v')
        if content[i][j] == 'w':
            cleanString += decode.get('w')
        if content[i][j] == 'x':
            cleanString += decode.get('x')
        if content[i][j] == 'y':
            cleanString += decode.get('y')
        if content[i][j] == 'z':
            cleanString += decode.get('z')
        if content[i][j] == ' ':
            cleanString += ' '

    outfile.write(cleanString + '\n')
    cleanString = ''
outfile.close()

