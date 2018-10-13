# import string

cypher = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' ', '\n':'\n'}
z = 'a'
# print cypher[z]

##x = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
##y = ''
##for i in range(len(x)):
##    y += cypher[x[i]]

inFile = open('A-small-attempt0.in', 'r')
outFile = open('output.out', 'w')

numCases = inFile.readline()
# print 'cases = ' + numCases
a = 1
for line in inFile:
    x = 'Case #' + str(a) + ": "
    for i in range(len(line)):
        x += cypher[line[i]]
    outFile.write(x)
    a += 1

inFile.close()
outFile.close()
# print x[1]

# print y

# abcdefghijklmnopqrstuvwxyz - coded
# yhesocvxduiglbkrztnwjpfmaq  - decoded
