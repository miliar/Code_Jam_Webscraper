




readfile = open("B-large.in")
writefile = open("output2.txt", "w")

lines = readfile.readlines()
assert int(lines[0]) == len(lines) - 1

for prob_num in xrange(1,len(lines)):
  line = str(int(lines[prob_num]))
  array = []
  for x in line:
    array.append(int(x))
  flag = 0
  while flag == 0:
    flag = 1
    for i in xrange(len(array)-1):
      if array[i] > array[i+1]:
        array[i] -= 1
        for j in xrange(i+1,len(array)):
          array[j] = 9
        flag = 0
        break
  string = ''
  for x in array:
    string = string + str(x)
  writefile.write("Case #%d: %d\n" % (prob_num, int(string)))
  
  
  
  
writefile.close()