import re

def solve(matrix):
  row_maxes = [max(x) for x in matrix]
  cols = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
  col_maxes = [max(x) for x in cols]
  for i in range(len(matrix)):
	for j in range(len(matrix[i])):
	  val = matrix[i][j]
	  if val != row_maxes[i] and val != col_maxes[j]:
		return "NO"
  return "YES"
	

def take_input(f):
  temp = re.split(" ",f.readline())
  x,y = int(temp[1]), int(temp[0])	
  matrix = []
  for i in range(y):
	line = f.readline()
	nums = [int(x.strip()) for x in re.split(" ",line)]
	matrix.append(nums)
  return matrix


output = []
with open("large.in","r") as f:
  trials = f.readline()
  for i in range(int(trials.strip())):
	state = take_input(f)
	outline = "Case #%d: %s" % (i+1, solve(state))
	print outline
	output.append(outline)
  with open("matrix2.out","w") as f:
	f.write("\n".join(output))


