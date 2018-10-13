f = open('B-large.in','rU')

line = f.readlines()
num = 0

for l in line[1:]:
  num = num + 1
  words = l.split(" ")
  
  com = {}
  opp = []

  for i in range(1,int(words[0])+1):
    com[words[i][0]+words[i][1]] = words[i][2]
    com[words[i][1]+words[i][0]] = words[i][2]

  words = words[int(words[0])+1:]
  for j in range(1,int(words[0])+1):
    opp.append(words[j])

  words = words[int(words[0])+1:]
 
  temp = words[1]
  
  l = len(temp)

  invoke = []

  for c in range(l-1):
    invoke.append(temp[c])
    
    if len(invoke) >= 2:
      check = invoke[-1]+invoke[-2]
      if check in com:
        invoke = invoke[:-2]
	invoke.append(com[check])

    for d in opp:
      if d[0] in invoke and d[1] in invoke:  
        invoke = []
  
  out = ""
  
  for i in invoke[:]:
    out=out + str(i)+', '

  out = out[:-2]
  print 'Case #'+str(num)+': '+'['+out+']'

f.close()

