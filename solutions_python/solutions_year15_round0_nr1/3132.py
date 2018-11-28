import sys

read_file = sys.argv[1]
write_file = read_file.split(".")[0] + ".out"

fi = open(read_file, "r")
fo = open(write_file, "w")

total_standing = 0
num_arr = []
friends = 0
counter = 0
num_sum = 0

for line in fi:
  
  if (len(line.split()) != 2):
    test_cases = len(line.split())
    continue
  
  processed_line = line.split()
  maximum_shyness = int(processed_line[0])
  for num in processed_line[1]:
    num_arr.append(int(num))
  
  if (len(num_arr) == 1):
    friends = 0
  else:
    for i in range(0, len(num_arr)):
      if num_arr[i] > 0:
	if (total_standing + friends) < i:
	  friends += (i-(total_standing+friends))
	total_standing += num_arr[i]
  fo.write("Case #%d: %d\n" % (counter+1, friends))
  
  friends = 0
  total_standing = 0
  num_arr = []
  counter += 1
  num_sum = 0
  
fo.close()
fi.close()
  

