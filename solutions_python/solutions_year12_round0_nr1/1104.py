code={'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r',
 'q': 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q',
 ' ': ' '}

def decode(s):
  s=list(s)
  for i in range(len(s)):
    s[i]=code[s[i]]
  s=''.join(s)
  return s

f = open('input.dat')
n=f.readline()
n=int(n)
for i in range(n):
  print "Case #"+str(i+1)+": "+decode(f.readline().strip())



    
