import sys

def process(inputfile, outputfile):
    f = open(inputfile, 'r')
    inputdata = f.readlines()
    f.close()

    it = iter(inputdata)

    #Number of cases
    N = int(it.next())

    t = {'y':'a', 'n':'b', 'q':'z', 'i':'d', 'c':'e', 'w':'f', 'l':'g', 'b':'h',
         'k':'i', 'u':'j', 'o':'k', 'm':'l', 'x':'m', 's':'n', 'e':'o', 'v':'p',
         'f':'c', 'p':'r', 'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x',
         'a':'y', 'z':'q'}
    
    fout = open(outputfile, 'w')

    for i in range(1, N+1):
        str1 = "Case #" + str(i) + ": "
        fout.write(str1)

        word = it.next()
        word2 = ''
        for c in word:
            word2 += t.get(c, ' ')

        fout.write(word2 + "\n")

    fout.close()
    
def main():
    if len(sys.argv) != 3:
        print 'usage: ./googlerese.py inputfile outputfile'
        sys.exit(1)

    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    process(inputfile, outputfile)

if __name__ == '__main__':
    main()
