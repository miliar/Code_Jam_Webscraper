f_in = open("qc3.input", 'r')  
f_out = open("qc3.output", 'w')

inputs = f_in.read().split('\n')
numOfTest = int(inputs[0])

def getNextInt(v, maxI):
  s = str(v)
  for i in range(1, len(s)):
    if s[i] <= maxI and s[i] != '0':
      return int(s[i:] + s[0:i])
  return -1


for linenum in range(numOfTest):
  line = inputs[linenum+1].split(' ')
  a = int(line[0])
  b = int(line[1])
  maxI = str(b)[0]
  idx = a
  count = 0
  while idx <= b:
    #print idx
    v = idx
    while True:
      v = getNextInt(v, maxI)
      #print v
      if idx == v or v == -1:
        break
      if v > b or v < idx:
        continue
      count += 1
      
    idx += 1
  lineout = "Case #" + str(linenum+1) + ": " + str(count)
  print lineout
  f_out.write(lineout+"\n")
  
f_out.close()
f_in.close()