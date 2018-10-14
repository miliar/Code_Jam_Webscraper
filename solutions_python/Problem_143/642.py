myfile = open("B-small-attempt0.in.txt", "r")
output = open("output.txt", "w")

total_cases = int(myfile.readline().strip())
for case_number in xrange(1, total_cases + 1):  
  [a, b, k] = myfile.readline().lower().split()
  count  = 0
  k = int(k)
  for i in range(int(a)):
    for j in range(int(b)):
      if i&j < k:
        count +=1
  output.write('Case #%d: %s' % (case_number, count) + "\n")

myfile.close()
output.close()
