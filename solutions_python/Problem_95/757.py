import sys

g = '''ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'''

e = '''our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'''

original = g
g = g.replace(' ','')
e = e.replace(' ', '')

m = {}
m['z'] = 'q'
m['q'] = 'z'
for i in range(len(g)):
  m[g[i]] = e[i]

def translate(dict, text):
  answer = ''
  for c in text:
    if c.isalpha():
      answer += dict[c]
    else:
      answer += c
  return answer

data = sys.stdin.readlines()

data = data[1:]
i = 1
for line in data:
  print("Case #" + str(i) + ': ' + translate(m, line))
  i += 1
