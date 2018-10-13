import sys
from string import maketrans

input = []
input.append("ejp mysljylc kd kxveddknmc re jsicpdrysi")
input.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
input.append("de kr kd eoya kw aej tysr re ujdr lkgc jv")

output = []
output.append("our language is impossible to understand")
output.append("there are twenty six factorial possibilities")
output.append("so it is okay if you want to just give up")

alphabet = {}
alphabet['q'] = "z"
alphabet['z'] = "q"

for index, item in enumerate(output):
  for cidx, char in enumerate(item):
    if char != " ":
      alphabet[char] = input[index][cidx]
#for letter in alphabet:
#  print letter, alphabet[letter]

target = "abcdefghijklmnopqrstuvwxyz"
source = ""

for c in target:
  source = source + alphabet[c]

#print target
#print source

transtable = maketrans(source,target)


for index, line in enumerate(open(sys.argv[1])):
  if index != 0:
    sys.stdout.write("Case #"+str(index)+": "+line.translate(transtable))
