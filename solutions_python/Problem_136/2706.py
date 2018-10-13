input = open('input.txt')
output = open('output.txt', 'w')

T = int(input.readline().strip())

for case in range(1,T+1):
  tokens = input.readline().strip().split(' ')
  C = float(tokens[0])
  F = float(tokens[1])
  X = float(tokens[2])
  
  min_time = X / 2.0
  f_time = 0
  done = False
  n = 0
  
  while not done:
    f_time += C / (2+n*F)
    t = f_time + X / (2+(n+1)*F)
    if t < min_time:
      min_time = t
      n+=1
    else:
      done = True 
  output.write('Case #' + str(case) + ': ' + str(min_time) + '\n')
  
input.close()
output.close()