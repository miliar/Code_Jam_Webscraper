def maxv(v):
  if v == 0:
    return 0
  if v % 3 == 0:
    return v / 3
  if v % 3 == 1:
    return v / 3 + 1
  if v % 3 == 2:
    return v / 3 + 1
    
def maxs(v):
  if v == 0:
    return 0
  if v % 3 == 0:
    return v / 3 + 1
  if v % 3 == 1:
    return v / 3 + 1
  if v % 3 == 2:
    return v / 3 + 2

f_in = open("qb3.input", 'r')  
f_out = open("qb3.output", 'w')

inputs = f_in.read().split('\n')
numOfTest = int(inputs[0])

for i in range(numOfTest):
  values = inputs[i+1].split(' ')
  print values
  numP = int(values[0])
  numS = int(values[1])
  thresh  = int(values[2])
  count = 0
  for j in range(3, numP+3):
    if maxv(int(values[j])) >= thresh:
      count += 1
    elif maxs(int(values[j])) >= thresh and numS > 0:
      count += 1
      numS -= 1
  lineout = "Case #" + str(i+1) + ": " + str(count)
  print lineout
  f_out.write(lineout+"\n")
    

f_out.close()
f_in.close()
