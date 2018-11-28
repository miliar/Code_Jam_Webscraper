import sys
LETTERS=26
filename=sys.argv[1]
f=open(filename,"r")

line=f.readline().split()
MAXL=int(line[0])
WORDS=int(line[1])
PATTERNS=int(line[2])

array=[]

for i in range(WORDS):
  array.append(f.readline())

for i in range(PATTERNS):
  n=0
  level=0
  pat=f.readline()
  pattern=[]
  for j in range(MAXL):
    if pat[level]!="(":
      pattern.append(pat[level])
    else:
      level+=1
      pattern.append("")
      while pat[level]!=")":
        pattern[j]+=pat[level]
        level+=1
    level+=1
        
  for j in array:
    ok=True
    for k in range(MAXL):
      if j[k] not in pattern[k]:
        ok=False
        break
    if ok: n+=1
  print "Case #%d: %d"%(i+1,n)

f.close()

