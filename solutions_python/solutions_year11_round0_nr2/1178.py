f = open('B-large.in','rU')

lines = f.readlines()
count = 0

for l in lines[1:]:
  count = count + 1
  words = l.split(" ")
  
  combine = {}
  oppose = []

  for i in range(1,int(words[0])+1):
    combine[words[i][0]+words[i][1]] = words[i][2]
    combine[words[i][1]+words[i][0]] = words[i][2]

  words = words[int(words[0])+1:]
  for j in range(1,int(words[0])+1):
    oppose.append(words[j])

  words = words[int(words[0])+1:]
 
  temp = words[1]
  
  l = len(temp)

  invoke = []

  for c in range(l-1):
    invoke.append(temp[c])
    
    if len(invoke) >= 2:
      check = invoke[-1]+invoke[-2]
      if check in combine:
        invoke = invoke[:-2]
	invoke.append(combine[check])

    for d in oppose:
      if d[0] in invoke and d[1] in invoke:  
        invoke = []
  
  out = ""
  
  for i in invoke[:]:
    out=out + str(i)+', '

  out = out[:-2]
  print 'Case #'+str(count)+': '+'['+out+']'

f.close()

