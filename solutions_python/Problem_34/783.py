def isMatchPattern(pattern, word):
  i=0
  j=0
  while i <len(pattern):
    alternatives=[]
    if pattern[i] == '(':
      i+=1
      while not pattern[i] == ')':
        alternatives.append(pattern[i]) 
        i+=1
    else:
      alternatives.append(pattern[i])
    try:
     alternatives.index(word[j])
    except Exception:
     return False
    j+=1
    i+=1 
  return True

fileIn=open('file.in','rt')
fileOut=open('file.out','wt')
index_line=fileIn.readline()
values=index_line.split(' ')
L=int(values[0])
D=int(values[1])
N=int(values[2])
words=[]
for i in xrange(D):
  word=fileIn.readline()
  if(word[-1] == '\r' or word[-1] == '\n'):
    word=str.join('',word[0:-1])
  words.append(word) 
for i in xrange(N):
  count=0
  pattern=fileIn.readline()
  if(pattern[-1] == '\r' or pattern[-1] == '\n'):
    pattern=str.join('',pattern[0:-1])
  for j in xrange(D):  
    if isMatchPattern(pattern,words[j]):
      count+=1
  fileOut.write('Case #'+str(i+1)+': '+str(count)+'\n')
  fileOut.flush()
fileIn.close()
fileOut.close()

