import string

inFileName = 'A-small-attempt0.in'

inFile = open(inFileName,'r')
outFile = open(inFileName.replace('.in','.out'),'w')

N = int(inFile.readline().strip())

print N

inText = ['z ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv']
outText = ['q our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up'] 

dic = {}

for i in range(3):
  for k in range(len(inText[i])):
    if ((inText[i][k] in string.letters) or (inText[i][k] == ' ')) and (inText[i][k] not in dic.keys()):
      dic[inText[i][k]] = outText[i][k]


missk = ''
missv = ''

for i in string.lowercase:
  if i not in dic.keys():
    missk = i
  if i not in dic.values():
    missv = i

dic[missk] = missv


for i in range(N):
  newline = ''
  for k in inFile.readline().strip():
    newline += dic[k]
  outFile.write('Case #' + str(i+1) + ': ' + newline + '\n')






