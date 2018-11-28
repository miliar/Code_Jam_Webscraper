# tongues.py
import sys

letters = {}
# samples and answers
s1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
a1 = 'our language is impossible to understand'

s2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
a2 = 'there are twenty six factorial possibilities'

s3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'
a3 = 'so it is okay if you want to just give up'

samples = [s1,s2,s3]
answers = [a1,a2,a3]

for i in range(len(samples)):
  for j,char in enumerate(samples[i]):
    letters[char] = answers[i][j]
    
# z is given
letters['z'] = 'q'
letters['q'] = 'z'

#print len(letters.keys())
  
T = int(sys.stdin.readline().strip())

for t in range(T):
  sentence = list(sys.stdin.readline().strip())
  for i,char in enumerate(sentence):
    sentence[i] = letters[char]
  print "Case #%d: %s" % (t+1,''.join(sentence))
