import sys

mapping = {
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
    ' ':' '
    }

  
N = sys.stdin.readline()

for case in range(0,int(N)):
  s = sys.stdin.readline()[:-1]
  res = ""

  for ch in s:
    res += mapping[ch]
  
  print "Case #%d: %s" % (case+1,res)

