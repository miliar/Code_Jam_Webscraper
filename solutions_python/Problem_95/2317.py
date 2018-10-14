from sys import stdin

replacing_letters = {
  'y': 'a',
  'n': 'b',
  'f': 'c',
  'i': 'd',
  'c': 'e',
  'w': 'f',
  'l': 'g',
  'b': 'h',
  'k': 'i',
  'u': 'j',
  'o': 'k',
  'm': 'l',
  'x': 'm',
  's': 'n',
  'e': 'o',
  'v': 'p',
  'z': 'q',
  'p': 'r',
  'd': 's',
  'r': 't',
  'j': 'u',
  'g': 'v',
  't': 'w',
  'h': 'x',
  'a': 'y',
  'q': 'z'
}

t = 0
for line in stdin.readlines():
  if t > 0:
    line = line.rstrip()
    out = ''
    for i in range(len(line)):
      if line[i] != ' ':
        try:
          out += replacing_letters[line[i]]
        except Exception:
          out += '-'
      else:
        out += ' '
    print 'Case #%i: %s' % (t, out)
    
  t += 1