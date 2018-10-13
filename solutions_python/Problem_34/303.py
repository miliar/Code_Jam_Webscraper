def addTrie(a,word,i):
  if i < len(word):
    try:
      a[word[i]]
    except:
      a[word[i]] = {}
    a[word[i]] = addTrie(a[word[i]],word,i+1)
    return a
  else:
    return 1


def patternize(b):
  s = []
  sgn = -1
  for i in b:
    if i == "(":
      sgn = 1
      s.append([])
      continue
    else: 
      if i == ")":
        sgn = -1
        continue
    if sgn == -1:
     s.append(i)
    else:
      s[len(s)-1].append(i)
  return s

def level(trie,pattern,c,occ):
  for i in trie.keys():
    if i in pattern[c]:
      if c == len(pattern)-1:
        occ += 1
      else:
        occ = level(trie[i],pattern,c+1,occ)
  return occ

#######

f = open("file.in","r")
g = open("file.out","w")
numbers = f.readline().rstrip("\n")
a = numbers.split(" ")
(l,d,n) = map(lambda x: int(x),a)

a = {}
for i in range(d):
  w = f.readline().rstrip("\n")
  a = addTrie(a,w,0)

for i in range(n):
  b = f.readline().rstrip("\n")
  s = patternize(b)
  g.write("Case #"+str(int(i+1))+": "+str(level(a,s,0,0))+"\n")
