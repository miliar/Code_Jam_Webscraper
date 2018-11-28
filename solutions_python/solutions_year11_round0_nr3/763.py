f = open('input.txt', 'r')
fout = open('output.txt', 'w')
n = int(f.readline())

test_vals = []
for i in xrange(22):
  test_vals.append(pow(2, i))
  
for i in xrange(0, n):
  m = int(f.readline())
  vals = f.readline().split()
  
  cnts = [0 for j in xrange(25)]
  
  sum = 0
  min = 1000000000
  
  for val in vals:
    i_val = int(val)
    sum += i_val
    if i_val < min: min = i_val
    
    j = 0
    for t_val in test_vals:      
      if (i_val & t_val) != 0:
        cnts[j] += 1
      j+=1  
  print(cnts)
  res = sum - min
    
  
  fout.write('Case #')
  fout.write(str(i + 1))
  fout.write(': ')
  good = True
  for c in cnts:
    if c % 2 != 0: 
      good = False
      break
  if good: fout.write(str(res))
  else: fout.write('NO')
  
  fout.write("\n")
	
fout.close()    
