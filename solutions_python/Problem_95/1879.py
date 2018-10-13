f = open('A-small.in','r')
cases = int(f.readline())

mapping = {'y': 'a', 'n': 'b', 'f': 'c', 'i': 'd', 'c': 'e', 'w': 'f', 'l': 'g', 'b': 'h', 'k': 'i', 'u': 'j',
           'o': 'k', 'm': 'l', 'x': 'm', 's': 'n', 'e': 'o', 'v': 'p', 'z': 'q', 'p': 'r', 'd': 's', 'r': 't',
           'j': 'u', 'g': 'v', 't': 'w', 'h': 'x', 'a': 'y', 'q': 'z', ' ': ' '}
for case in range(1, cases+1):
  line = f.readline()[:-1]
  letters = []
  for c in line:
    letters.append(mapping[c])
  english = ''.join(letters)
  print 'Case #{}: {}'.format(case, english)
