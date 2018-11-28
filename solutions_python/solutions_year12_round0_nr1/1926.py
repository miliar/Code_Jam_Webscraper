import sys

class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg

def main(argv=None):

  dict = {'y':'a',
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
          'q':'z',
          ' ':' '}

  try:
    filename = 'data.txt'
    file = open(filename, 'r')
    nTestCases = int(file.readline().rstrip())

    outfile = open('answer.txt', 'w')

    for i in xrange(nTestCases):
      inLine = file.readline().rstrip()
      out = []
      for j in inLine:
        out.append( dict[j])
      outfile.write('Case #{0}: {1}\n'.format(i+1, ''.join(out)))
  except:
    print sys.stderr
    return 2

if __name__ == "__main__":
    sys.exit(main())

