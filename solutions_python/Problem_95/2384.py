trans = {'q': 'z', 'z': 'q', ' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
n = input()
for i in xrange(n):
  s = raw_input()
  res = ''
  for j in range(len(s)):
    res += trans[s[j]]
  print 'Case #' + str(i+1) + ': ' + res
