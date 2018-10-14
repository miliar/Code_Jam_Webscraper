#    googlereseText = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
#    normalText = translate(googlereseText)
#    print normalText
import sys

def translate(stringG):
    newString = ''

    mapps = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v',
             'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b',
             'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j',
             'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q'}
    for letter in stringG:
        if letter == '\n': continue
        if letter == ' ': newString += ' '

        else:
            newString += mapps[letter]

    return newString


if __name__ == "__main__":
    f = sys.stdin
    output = open('A-small.txt', 'w')
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)
    result = []
    test = int(f.readline())
    for t in xrange(test):
        s = f.readline()
        output.write("Case #%d: %s \n" % (t+1,translate(s)))

    output.close()



