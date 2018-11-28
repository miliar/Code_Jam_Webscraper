t = int(raw_input())

google = {'a':'y', 'b':'h', 'c':'e', 'd':'s',
          'e':'o', 'f':'c', 'g':'v', 'h':'x',
          'i':'d', 'j':'u', 'k':'i', 'l':'g',
          'm':'l', 'n':'b', 'o':'k', 'p':'r',
          'q':'z', 'r':'t', 's':'n', 't':'w',
          'u':'j', 'v':'p', 'w':'f', 'x':'m',
          'y':'a', 'z':'q', ' ':' '}

for i in xrange(t):
    sentence = list(raw_input())
    sentence = [google[alphabet] for alphabet in sentence]
    sentence = ''.join(sentence)
    print "Case #" + str(i+1) + ": " + sentence
