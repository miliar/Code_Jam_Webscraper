numtests = int(raw_input())
test_data = []
for i in range(numtests):
  temp = raw_input().split()
  test_data.append([temp[0],int(temp[1])])

for a in range(len(test_data)):
  num_flips = test_data[a][1]
  table = test_data[a][0]
  num_attempts = 0
  stop = False
  while(stop==False):
    first_sad = str.find(table,'-')
    if first_sad == -1:
      print "Case #"+str(a+1)+": "+str(num_attempts)
      stop=True
      break
    elif first_sad >= (len(table)-num_flips+1):
      print "Case #"+str(a+1)+": "+"IMPOSSIBLE"
      stop=True
      break
    else:
      temp = list(table)
      for i in range(first_sad,first_sad+num_flips):
        if(temp[i]=='-'):
          temp[i] = '+'
        else:
          temp[i] ='-'
      table = ''.join(temp)
      num_attempts += 1