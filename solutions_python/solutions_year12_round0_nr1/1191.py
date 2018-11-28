## translate problem google space jam with michael jordan


dictionary = {'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l',
              'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x', 'a':'y', 'q':'z', ' ':' '}

data = open ('/Users/Andrew/Desktop/A-small-attempt0.in', 'r')
numberOfLines = int(data.readline())

for index, line in enumerate(data):
    translatedLine = ''
    for character in line:
        if (character != '\n'):
            translatedLine += dictionary[character]

    print 'Case #%d: %s' %(index+1, translatedLine)

data.close()



        


