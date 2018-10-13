#!/usr/bin/env python
# Marco Gallotta

with open('A.in', 'r') as file:
  input = file.readlines()[1:]
with open('A.out', 'r') as file:
  output = [l[9:] for l in file.readlines()]

decode = {
    'y': 'a',
    'e': 'o',
    'q': 'z',
    'z': 'q',
    }
for inp, out in zip(input, output):
  for i, o in zip(inp, out):
    decode[i] = o
for a in 'qwerttyuioplkjhgfdsazxcvbnm':
  if a not in decode.values():
    print a

N = int(raw_input())
for case in xrange(N):
  line = raw_input()
  ans = [decode[c] for c in line]
  print 'Case #%d: %s' % (case+1, ''.join(ans))
