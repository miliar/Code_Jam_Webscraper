input = open('input.txt')
output = open('output.txt', 'w')

T = int(input.readline().strip())

for t in range(0,T):
  choice1 = int(input.readline().strip())
  for r in range(0,choice1-1):
    input.readline()
  set1 = set(input.readline().strip().split(' '))
  for r in range(choice1,4):
    input.readline()
  choice2 = int(input.readline().strip())
  for r in range(0,choice2-1):
    input.readline()
  set2 = set(input.readline().strip().split(' '))
  for r in range(choice2,4):
    input.readline()
  p = set1.intersection(set2)
  if len(p) == 0:
    output.write('Case #' + str(t+1) + ': ' + 'Volunteer cheated!')
  elif len(p) > 1:
    output.write('Case #' + str(t+1) + ': ' + 'Bad magician!')
  else:
    output.write('Case #' + str(t+1) + ': ' + p.pop())
  output.write('\n')
	
input.close()
output.close()