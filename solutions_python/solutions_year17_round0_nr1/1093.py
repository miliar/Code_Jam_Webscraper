def opposite(c):
  if c == '+': return '-'
  else: return '+'

def count_flips(S, k):
  S_chars = []
  for c in S:
    S_chars.append(c)
  num_flips = 0
  remaining_len = len(S)
  index = 0
  while True:
    # keep scanning until you find a -
    for i in xrange(remaining_len):
      if S_chars[index] == '+':
        remaining_len -= 1
        index += 1
      else:
        # impossible if not enough left
        if remaining_len < k:
          return -1
        else:
          # flip
          for j in xrange(k):
            S_chars[index+j] = opposite(S_chars[index+j])
          num_flips += 1
    if remaining_len == 0:
      return num_flips

with open('A-large.in', 'r') as f:
  with open('A_large.out', 'w') as out:
    lines = [ x.strip() for x in f.readlines() ]
    T = int(lines[0])
    for i in xrange(T):
      line = lines[i+1] # case i+1
      data = line.split(' ')
      S, k = data[0], int(data[1])
      num_flips = count_flips(S, k)
      if num_flips >= 0:
        out.write('Case #%d: %d\n' % (i+1, num_flips))
      else:
        out.write('Case #%d: IMPOSSIBLE\n' % (i+1))
