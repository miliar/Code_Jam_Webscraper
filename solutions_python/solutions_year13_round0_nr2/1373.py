def solve(**kwargs):
  
  N = kwargs['N']
  M = kwargs['M']
  lawn = kwargs['lawn']
  
  levels = []
  
  for i in lawn:
    for o in i:
      if o not in levels:
	levels.append(o)
  
  levels.sort()
  
  for level in levels:
    for i in range(N):
      flag = True
      o = 0
      while flag and o < M:
	flag = flag and lawn[i][o] in (level,0)
	if 0 < lawn[i][o] < level:
	  return 'NO'
	o += 1
      if flag:
	for u in range(M):
	  lawn[i][u] = 0
    for i in range(M):
      flag = True
      o = 0
      while flag and o < N:
	flag = flag and lawn[o][i] in (level,0)
	if 0 < lawn[o][i] < level:
	  return 'NO'
	o += 1
      if flag:
	for u in range(N):
	  lawn[u][i] = 0
  
  return 'YES'

if __name__ == "__main__":
  
  f_in = open('file.in','r')
  f_out = open('file.out','w')

  T = int(f_in.readline())

  for i in range(T):
    
    problem = {}
    
    problem['lawn'] = []
    
    [problem['N'],problem['M']] = [int(t) for t in f_in.readline().split(' ')]
    
    for o in range(problem['N']):
      problem['lawn'].append([int(t) for t in f_in.readline().split(' ')])
    
    f_out.write('Case #' + str(i + 1) + ': ' + solve(**problem) + '\n')

  f_in.close()
  f_out.close