
data = open("C-large.in", "r")
myout = open("candy_out.txt", "w")
cases = int( data.readline() )

best_split = 0
for ct in range(0, cases):
  array_size = int( data.readline() )
  array = list(map( lambda x: int(x), data.readline().split() ) )
  array.sort()
  
  no_split = True
  for split_position in range(1, len(array)):
    dumb_sum_1 = dumb_sum_2 = 0
    smart_sum_1 = smart_sum_2 = 0
    for i in range(0, split_position):
      #print(array[i], " ", end="")
      dumb_sum_1 = (dumb_sum_1 ^ array[i])
      smart_sum_1 += array[i]
    #print("|",end="")
    for i in range(split_position, len(array)):
      #print(array[i], " ", end="")
      dumb_sum_2 = (dumb_sum_2 ^ array[i])
      smart_sum_2 += array[i]
    #print("")
    if dumb_sum_1 == dumb_sum_2:
      no_split = False
      best_split = split_position
      break
  myout.write("Case #" + str(ct+1) + ": ")
  if no_split == True:
    myout.write("NO" + '\n')
  else:
    myout.write(str(smart_sum_2) + '\n')