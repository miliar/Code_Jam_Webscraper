#!/usr/bin/python
import bisect

def check_partial(word, words):
  ind = bisect.bisect_left(words, word)
  return ind != len(words) and words[ind][:len(word)] == word

def gen_words(word, all_words):
  def _gen_words(i, cur, words):
    if i >= len(word):
      words.append(cur)
      return
    if word[i] != '(':
      nw = cur + word[i]
      if check_partial(nw, all_words):
        _gen_words(i+1, nw, words)
      return
    i += 1
    paren = word.find(')', i)
    assert paren != -1
    while i < paren:
      nw = cur + word[i]
      if not check_partial(nw, all_words):
        i += 1
        continue
      _gen_words(paren+1, nw, words)
      i += 1
  words = []
  _gen_words(0, '', words)
  return words
    

f = open('A-large.in', 'r')
lines = [line.strip() for line in f.readlines()]
f.close()

L, D, N = map(int, lines[0].split(' '))
words = []
for word in lines[1:1+D]:
  words.append(word)
words.sort()

case = 1
f = open('A-large.out', 'w')
for word in lines[1+D:]:
  all_possible = gen_words(word, words)
  f.write('Case #%d: %d\n' % (case, len(all_possible)))
  case += 1
