TYPE = "large"

in_file = open("..\\input\\2012-qual-B-%s.txt" % TYPE, "r")
out_file = open("..\\output\\2012-qual-B-%s.txt" % TYPE, "w")

num_cases = int(in_file.readline().strip())

for case in range(num_cases):
  answer = 0
  
  input = in_file.readline().strip().split(' ')
  N = int(input[0])
  S = int(input[1])
  p = int(input[2])
  totals = [int(total) for total in input[3:]]
  
  total_not_surprising = 0
  total_surprising = 0
  
  for total in totals:   
    if total >= (3 * p) - 2 and total >= p:
      total_not_surprising += 1
    elif total >= (3 * p) - 4 and total >= p:
      total_surprising += 1
    
  answer = total_not_surprising + min(S, total_surprising)
    
  out_file.write("Case #%s: %s\n" % (case + 1, answer))
    
in_file.close()
out_file.close()

print "Done!"