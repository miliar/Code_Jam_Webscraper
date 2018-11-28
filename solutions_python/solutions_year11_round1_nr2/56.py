#!/usr/bin/env python

import sys

_rest_tokens = []

def readToken():
  global _rest_tokens
  if not _rest_tokens:
    _rest_tokens = sys.stdin.readline().strip().split()
    _rest_tokens.reverse()
  return _rest_tokens.pop()

def log(*obj):
  str_obj = [str(o) for o in obj]
  sys.stderr.write(' '.join(str_obj) + '\n')

class Word(object):
  def __init__(self, word):
    self.word = word
    self.letters = set(list(word))
    self.len = len(word)
  
  def __str__(self):
    return self.word
    
  def __repr__(self):
    return self.word
  
cmp_cache = None
  
def cmp_by_letter(word1, word2, letter):
  if word2 in cmp_cache[word1][letter]:
    result = cmp_cache[word1][letter][word2]
  else:
    result = True
    for i in xrange(len(word1)):
      if (word1[i] == letter and word2[i] != letter) or (word1[i] != letter and word2[i] == letter):
        result = False
        break
    cmp_cache[word1][letter][word2] = result
    cmp_cache[word2][letter][word1] = result
  return result
  
def process(word, seq, sd):
  sd = filter(lambda w: w.len == word.len, sd)
  if len(sd) == 1:
    return 0
  ans = 0
  for letter in seq:
    found = False
    for w in sd:
      if letter in w.letters:
        found = True
        break
    if found:
      if letter in word.letters:
        sd = filter(lambda w: cmp_by_letter(w.word, word.word, letter), sd)
      else:
        ans += 1
        sd = filter(lambda w: not letter in w.letters, sd)
    if len(sd) == 1:
      break
  return ans
    
def main():
  global cmp_cache
  case_count = int(readToken())
  for i in range(case_count):
    log('Process case #%d' % (i + 1))
    d = []
    s = []
    n = int(readToken())
    m = int(readToken())
    cmp_cache = {}
    for j in xrange(n):
      w = readToken()
      d.append(w)
      cache = {}
      for k in xrange(27):
        cache[chr(ord('a') + k)] = {}
      cmp_cache[w] = cache
    for j in xrange(m):
      s.append(readToken())
    sd = [Word(x) for x in d]
    result = []
    for seq in s:
      ans = 0
      ans_word = None
      for word in sd:
        r = process(word, seq, sd)
        if r > ans or not ans_word:
          ans = r
          ans_word = word.word
      result.append(ans_word)  
    print 'Case #%d: %s' % (i + 1, ' '.join(result))
      
if __name__ == '__main__':
  main()
