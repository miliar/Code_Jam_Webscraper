
input_file_name = "B-small-attempt0.in"
output_file_name = "B-small-attempt0_output.txt"

# ---------------------------------------------


input_file = open(input_file_name, "r")
output_file = open(output_file_name, "wb")



content = input_file.readlines()

content_str = []
for line in content:
  content_str.append(line.rstrip())
#


# count the test cases
loop_count = int(content_str[0])
current_loop_count = 0
test_case_factor = 1

while current_loop_count<loop_count:
  
  line_to_check = 1+test_case_factor*current_loop_count # for content_str
  
  temp_str = content_str[line_to_check]
  
  temp_str_list = temp_str.split(' ')
  
  total_time = 0.0
  c = float(temp_str_list[0]) # cost per farm
  f = float(temp_str_list[1]) # increment per new farm
  x = float(temp_str_list[2]) # total cookies
  
  
  principle_value = float(x/2)
  
  f_count = 0.0
  while True:
    
    new_value = float(x /( 2+f*(f_count+1) ))
    
    f_count_copy = f_count
    while f_count_copy >= 0:
      new_value_portion = float(c/(2+f*f_count_copy))
      new_value += new_value_portion
      f_count_copy -= 1
    
    
    if principle_value > new_value:
      principle_value = new_value
      f_count += 1
      continue
    else:
      break
  
  
  output_file.write("Case #%d: %f\n" % (current_loop_count+1, principle_value))
  
  print "Case #%d: %f\n" % (current_loop_count+1, principle_value)
  
  
  current_loop_count += 1



input_file.close()
output_file.close()
