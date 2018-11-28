import sys

input_file = open(sys.argv[1], "r")
output_file = open(sys.argv[2], "w")

try:
  num_cases = int(input_file.readline())
  for case in range(num_cases):
    num_standing = 0 
    num_added = 0
    
    curr_case = input_file.readline().split()
    curr_max_shy = int(curr_case[0]) + 1
    shy_vals = curr_case[1]
    
    for i in range(curr_max_shy):
      if (num_standing >= i):
        num_standing += int(shy_vals[i])       
      else:
        num_added += 1
        num_standing += 1
        num_standing += int(shy_vals[i])

    case_response = "Case #%d: %d\n" % (case + 1, num_added)
    output_file.write(case_response)

finally:
  input_file.close()
  output_file.close()