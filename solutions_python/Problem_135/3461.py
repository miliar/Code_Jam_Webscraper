
input_file_name = "A-small-attempt0.in"
output_file_name = "output_a_small.txt"

# ---------------------------------------------


input_file = open(input_file_name, "r")
output_file = open(output_file_name, "wb")



content = input_file.readlines()

content_str = []
for line in content:
  content_str.append(line.rstrip())
#



loop_count = int(content_str[0])
current_loop_count = 0

while current_loop_count<loop_count:
  
  line_to_check = 1+10*current_loop_count # for content_str
  
  temp_input = int(content_str[line_to_check])
  
  temp_str = content_str[line_to_check + temp_input]
  
  temp_str_list = temp_str.split(' ')
  
  
  matched = 0
  matched_item = 0
  
  
  line_to_check = 1+10*current_loop_count + 5  # for content_str
  temp_input_second = int(content_str[line_to_check])
  
  temp_str_second = content_str[line_to_check + temp_input_second]
  
  temp_str_list_second = temp_str_second.split(' ')
  for item in temp_str_list_second:
    if item in temp_str_list:
      matched += 1
      matched_item = int(item)
  
  if matched == 1:
    print "Case #%d: %d" % (current_loop_count+1, matched_item)
    output_file.write("Case #%d: %d\n" % (current_loop_count+1, matched_item))
  elif matched == 0:
    print "Case #%d: Volunteer cheated!" % (current_loop_count+1)
    output_file.write("Case #%d: Volunteer cheated!\n" % (current_loop_count+1))
  else:
    print "Case #%d: Bad magician!" % (current_loop_count+1)
    output_file.write("Case #%d: Bad magician!\n" % (current_loop_count+1))
  
  
  current_loop_count += 1
  matched = 0



input_file.close()
output_file.close()
