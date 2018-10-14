import re

def match(word, words):
  word = word.replace("(","[")
  word = word.replace(")","]")
  
  value = 0
  for i in words:
    val = re.search(word, i)
    if val != None:
      value += 1
  return value

f = open("quad1.test", "r")
f = f.read()
f = f.split()

L = int(f[0])
D = int(f[1])
N = int(f[2])

words = []
for i in range(3,3+D):
  words.append(f[i])
  
for i in range(3+D, 3+D+N):
  word = f[i]
  values = match(word, words)
  print "Case #" + str(i-2-D) + ": " + str(values)
 
