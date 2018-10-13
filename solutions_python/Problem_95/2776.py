import sys

#in_put = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
#out_put = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

i = 0
#key = dict()
key = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}

#for g in in_put:
#  key[g] = out_put[i]
#  i += 1

key['q'] = 'z'
key['z'] = 'q'

#f = open("input", "r")
f = sys.stdin
num_lines = f.readline()
i = 0
for line in f:
  translation = ''
  for c in line:
    if(c != '\n'):
      translation = translation + key[c]
  i = i + 1
  print "Case #" + str(i) + ": " + translation
