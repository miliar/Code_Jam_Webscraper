
import sys

# Alien language

if __name__ == '__main__':
  fin = open(sys.argv[1], 'r')
  [L, D, N] = [int(x) for x in fin.readline().strip().split()]
  words = dict()
  for _ in xrange(D):
    word = fin.readline().strip()
    d = words
    for letter in word:
      if letter not in d.keys():
        d[letter] = dict()
      d = d[letter]
  case = 1
  fout = open(sys.argv[1] + '.out', 'w')
  for _ in xrange(N):
    pattern = fin.readline().strip()
    #print pattern
    possible_words = None
    d = words
    possible_words_new = []
    while len(pattern) > 0:
      if pattern[0] == '(':
        end = pattern.index(')')
        options = [c for c in pattern[1:end]]
        pattern = pattern[end+1:]
      elif pattern[0] in ['\n', '\r', '\0']:
        break
      else:
        options = [pattern[0]]
        pattern = pattern[1:]
      options = list(set(options))
      if possible_words is None:
        possible_words = []
        for option in options:
          if option in words.keys():
            possible_words.append(option)
      else:
        for w in possible_words:
          #print w
          d = words
          for c in w:
            #print words, possible_words, options
            d = d[c]
          for option in options:
            if option in d.keys():
              nw = w + option
              #print nw
              possible_words_new.append(nw)
        possible_words = possible_words_new
        possible_words_new = []
    fout.write('Case #%i: %i\n' % (case, len(possible_words)))
    #print possible_words
    case += 1
  fout.close()
  fin.close()
