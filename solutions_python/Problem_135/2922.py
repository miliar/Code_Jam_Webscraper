input = open('A-small-attempt1.in')

test_num = int(input.readline().split()[0])

array = []
for line in input:
  array.append([int(x) for x in line.split()])

for i in range(test_num):
  line1 = array[array[0 + i*10][0] + i*10]
  line2 = array[array[5 + i*10][0] + 5 + i*10]
  common_ans = set(line1) & set(line2)
  length = len(common_ans)

  if length == 1:
  	print 'Case #', i+1, ':', common_ans.pop()
  elif length > 1:
  	print 'Case #', i+1, ': Bad magician!'
  else:
    print 'Case #', i+1, ': Volunteer cheated!'
    
