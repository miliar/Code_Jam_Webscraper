def rotate(n, num_digits):
  n_str = str(n)
  
  while len(n_str) < num_digits:
    n_str = '0' + n_str
  
  n_last = len(n_str) - 1
  n_str = n_str[n_last]+ n_str[:n_last]
  return int(n_str)  

TYPE = "large"

in_file = open("..\\input\\2012-qual-C-%s.txt" % TYPE, "r")
out_file = open("..\\output\\2012-qual-C-%s.txt" % TYPE, "w")

num_cases = int(in_file.readline().strip())

for case in range(num_cases):
  answer = 0
  
  input = in_file.readline().strip().split(' ')
  A = int(input[0])
  B = int(input[1])
  num_digits = len(input[0])
  
  for m in range(A, B - 1):
    n = m
    this_m = []
    
    for ii in range(1, num_digits):
      n = rotate(n, num_digits)
      if n > m and n <= B and n not in this_m:
        this_m.append(n)
        answer += 1
        
  out_file.write("Case #%s: %s\n" % (case + 1, answer))
    
in_file.close()
out_file.close()

print "Done!"