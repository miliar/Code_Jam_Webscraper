import re

f = open('A-small-attempt0.in.txt', 'r')
slug = f.readline()
words = 25 
cases = 10 

wordlist = []
for i in xrange(words):
  wordlist.append(f.readline())

caselist = []
for i in xrange(cases):
  caselist.append(f.readline())

for i, case in enumerate(caselist):
  score = 0
  
  def subFunct(obj):
    ls = obj.group(0)
    return '(' + '|'.join(list(ls[1:-1])) + ')'

  patt = re.sub(r'\(.+?\)', subFunct, case)

  for word in wordlist:
    patt = re.compile(patt)
    matches = re.findall(patt, word)
    score = score + len(matches)

  print 'Case #%s: %s' % (i+1, score)
