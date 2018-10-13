#! /usr/bin/python

import sys
import copy

def possible_combos(case, possible_words):
  case = case.strip()
  tokenized = tokenize(case)
  count = recurse('', tokenized)
  return count

def is_word(word):
  return word in possible_words

def is_word_prefix(word):
  for possib_word in possible_words:
    if possib_word.startswith(word):
      return True

def recurse(prefix, remaining):
  #print "%s: %r" % (prefix, remaining)
  if len(prefix) > 0 and not is_word_prefix(prefix):
    return 0
  remaining = copy.copy(remaining)
  if not remaining:
    if is_word(prefix):
      #print "found word: %s" % prefix
      return 1
    else:
      #print "not a word: %s" % prefix
      return 0

  current_set = remaining.pop(0)
  results = 0
  for char in current_set:
    results += recurse(prefix + char, remaining)

  return results

def tokenize(case):
  result = []
  set = None
  for char in case:
    if char == '(':
      set = []
    elif char == ')':
      result.append(set)
      set = None
    elif set is not None:
      set.append(char)
    else:
      result.append([char])
    #print "char: %s result: %r set: %r" % (char, result, set)
  return result

filename = sys.argv[1]
lines = open(filename).readlines()
(word_len, num_words, num_cases) = [int(x) for x in lines.pop(0).split(' ')]
possible_words = [x.strip() for x in lines[0:num_words]]
test_cases = lines[num_words:num_words+num_cases]

i = 1
for case in test_cases:
  print "Case #%d: %d" % (i, possible_combos(case, possible_words))
  i += 1
