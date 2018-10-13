#!/usr/bin/env python

class alien_dict:
  valid_letters = []
  word_len = 0
  def __init__(self, words):
    self.word_len = len(words[0])
    self.valid_letters = []
    for i in range(0, self.word_len + 1):
      self.valid_letters.append({})
      for word in words:
        prefix = word[:i]
        if not self.valid_letters[i].has_key(prefix):
          self.valid_letters[i][prefix] = True

  def split_word(self, word):
    result = []
    pos = 0
    while pos < len(word):
      if '(' == word[pos]:
        subresult = []
        pos += 1
        while word[pos] != ')':
          subresult.append(word[pos])
          pos += 1
        result.append(tuple(subresult))
        pos += 1
      else:
        result.append((word[pos],))
        pos += 1
    return result

  def pattern_match_count(self, prefix, pattern):
    result = 0
    if len(pattern) == 1:
      for letter in pattern[0]:
        if self.valid_letters[self.word_len].has_key(prefix + letter):
          result += 1
      return result

    result = 0
    for letter in pattern[0]:
      if self.valid_letters[len(prefix) + 1].has_key(prefix + letter):
        result += self.pattern_match_count(prefix + letter, pattern[1:])
    return result    

  def match_count(self, word):
    return self.pattern_match_count('', self.split_word(word))

input = open("A-large.in", "r")
lines = input.readlines()

D = int(lines[0].split(" ")[1])
words = []
for i in range(1, D + 1):
  words.append(lines[i].strip('\n'))

ad = alien_dict(words)
for i in range(D + 1, len(lines)):
   result = ad.match_count(lines[i].strip('\n'))
   print 'Case #%i: %i' % (i - D, result)

#  result = count(lines[i], "welcome to code jam")
#  print result
#  resultstr = ('%04d' % result)[-4:]
#  print 'Case #%i: %s' % (i, resultstr)

