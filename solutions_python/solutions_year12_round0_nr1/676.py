from sys import argv


def main():
  f = open(argv[1], 'r')
  casecount = int(f.readline())
  count = 0
  mymap = {
    'a':'y',
    'b':'h',
    'c':'e',
    'd':'s',
    'e':'o',
    'f':'c',
    'g':'v',
    'h':'x',
    'i':'d',
    'j':'u',
    'k':'i',
    'l':'g',
    'm':'l',
    'n':'b',
    'o':'k',
    'p':'r',
    'q':'z',
    'r':'t',
    's':'n',
    't':'w',
    'u':'j',
    'v':'p',
    'w':'f',
    'x':'m',
    'y':'a',
    'z':'q',
    ' ':' ',
    "\n":"\n",
    }
  while casecount:
    count = count + 1
    casecount = casecount - 1

    data_line = f.readline().rstrip("\n")
    data_line.strip()
    letters = list(data_line)

    new_line = []
    for l in letters:
      new_line.append(mymap[l])

    print "Case #%d: %s" % (count, ''.join(new_line))


if __name__ == "__main__":
  main()
