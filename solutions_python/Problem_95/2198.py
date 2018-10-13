# Create map
import operator

algorithm = {}
lang = []
lang.append("ejp mysljylc kd kxveddknmc re jsicpdrysi")
lang.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
lang.append("de kr kd eoya kw aej tysr re ujdr lkgc jv")
translate = []
translate.append("our language is impossible to understand")
translate.append("there are twenty six factorial possibilities")
translate.append("so it is okay if you want to just give up")

algorithm['z'] = 'q'
algorithm['q'] = 'z'
algorithm['\n'] = '\n'

for i in range(3):
  for j in range(len(lang[i])):
    algorithm[lang[i][j]] = translate[i][j]

# Solve problem
f = open('small.in', 'r')
lines = []
answer = []

for line in f.readlines():
  lines.append(line)
lines.pop(0)

for line in lines:
  answer.append("")
  for letter in line:
    answer[-1] += algorithm[letter]
  print answer[-1]

f = open('out.out', 'w')
for test in range(len(answer)):
  f.write("Case #{0}: {1}".format(test + 1, answer[test]))
