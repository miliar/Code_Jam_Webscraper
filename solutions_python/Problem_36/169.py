SENTENCE = "welcome to code jam"
LETTERS = ''.join(set(SENTENCE))

import re
clean_re = re.compile('[^'+LETTERS+']')

def suffixes(s):
  if len(s)>1:
    for i in suffixes(s[1:]):
      yield i
  yield s

def calculate(line, sentence):
  cleaned = clean_re.sub('', line)
  
  indexes = dict((l,[]) for l in LETTERS)
  for i,c in enumerate(cleaned):
    indexes[c].append(i)
    
  count=dict((suffix,[0]*len(cleaned)) for suffix in suffixes(sentence))
  
  for suffix in list(suffixes(sentence)):
    cnt = count[suffix]
    last = len(cleaned)
    n=0
    for pos in reversed(indexes[suffix[0]]):
      cnt[pos+1:last] = [n]*(last-pos-1)
      last_suff = suffix[1:]
      if last_suff:
        last_cnt = count[last_suff][pos] if last_suff else 0
        n = n + last_cnt
      else:
        n+=1
      last = pos+1
    cnt[0:last] = [n]*last
  return count[sentence][0] if count[sentence] else 0

import sys
input = len(sys.argv)>1 and open(sys.argv[1]) or sys.stdin

N = int(input.readline())
for i in xrange(N):
  print "Case #%d: %04d"%(i+1,calculate(input.readline(),SENTENCE)%10000)
