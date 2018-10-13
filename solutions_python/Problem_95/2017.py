def replacer(letter):
    dict1 = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v', 'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', '\n':'',
             'n':'b', 'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j', 'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' '}
    return dict1[letter]

fileread = open('A-small-attempt1.in', 'r')
filewrite = open('A-small-attempt1-output.txt', 'w')

i = 1
n = int(fileread.readline()[:-1])

while i <= n:
    sentence = list(fileread.readline())[:-1]
    k = 0
    while k < len(sentence):
        sentence[k] = replacer(sentence[k])
        k += 1
    filewrite.write('Case #' + str(i) + ': ' + ''.join(sentence) + '\n')
    i += 1
    
fileread.close()
filewrite.close()
