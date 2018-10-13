import sys
#b = '(ab)cd(efg)hi(jk)' #hack

f = sys.stdin

contents =  f.read()

lst = contents.split("\n")

items = lst[0].split(" ")

L = int(items[0])
D = int(items[1])
N = int(items[2])

#print L, D, N

words = set()
i=0
while i < D:
  i+=1
  wd = lst[i]
  for j in xrange(1,len(wd)+1):
    words.add(wd[:j])

#print words

def parseWord(wd):
  out = []
  paren = False
  cur = ""
  for i in xrange(len(wd)):
    if wd[i] == '(':
      paren = True
    elif wd[i] == ')':
      paren = False
      out.append(cur)
      cur =""
    else:
       cur = cur+wd[i]
       if not paren:
         out.append(cur)
	 cur=""
  return out
       

ctr = 0

def testCase(wd):
  wd = parseWord(wd)
  if len(wd) != L:
    return 0 
  global ctr
  ctr = 0
  
  def helper(cur, idx):    
    global ctr
    if idx == L:
      ctr+=1
      return
    t = wd[idx]
    for i in xrange(len(t)):
      nw = cur + t[i]
      if nw in words:
	helper(nw,idx+1)
  
  helper('',0)  
  return ctr

#print D+ N + 1
while i < D + N + 1:
  i+=1  
  w = lst[i]
  cnt = testCase(w)
  if cnt >= 0:
    #print i, w
    print 'Case #%d: %d' % (i-D, cnt)
  