
def solve(**kwargs):
  
  S_max = kwargs['S_max']
  S_count = [int(i) for i in kwargs['S_count']]
  
  total = sum([int(i) for i in S_count])
  i = needed = stood = 0
  while(i <= S_max and stood < S_max):
    if S_count[i] != 0:
      if stood + needed < i:
	needed += 1
      else:
	stood += S_count[i]
	i += 1
    else:
      i += 1
    
  return str(needed)

if __name__ == "__main__":
  
  f_in = open('file.in','r')
  f_out = open('file.out','w')
  
  T = int(f_in.readline())
  
  for i in range(T):
    
    problem = {}
    line = f_in.readline()
    
    problem['S_max'] = int(line.split(' ')[0])
    problem['S_count'] = line.split(' ')[1].replace('\n','')
    
    f_out.write('Case #' + str(i + 1) + ': ' + solve(**problem) + '\n')

  f_in.close()
  f_out.close