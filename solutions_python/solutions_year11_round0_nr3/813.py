
#
def calculate_candy_split(number_list):
  xor_all_number = 0
  lowest_number = number_list[0]
  running_sum = 0

  for number in number_list:
    xor_all_number=xor_all_number^number
    running_sum = running_sum+number
    
    if lowest_number>number:
        lowest_number = number

  if xor_all_number!=0:
      return_value="NO"
  else:
      return_value=str(running_sum-lowest_number)

  return return_value

#file_handle = open('candy_splitting_test_input.txt','r')
#output_file_handle = open('candy_splitting_test_output.txt','w')
file_handle = open('candy_splitting_C-large.in','r')
output_file_handle = open('candy_splitting_C-large.out','w')


#number_list = [1, 2, 3, 4, 5]
#number_list = [3, 5, 6]

number_of_inputs = int(file_handle.readline())

case_counter = 0
while case_counter < number_of_inputs:

  number_list = []
    
  number_of_entries = int(file_handle.readline())
  string_number_list = file_handle.readline().split(' ')
  for string in string_number_list:
    number_list.append(int(string))
    
  case_counter = case_counter+1
    
  #print('Case #'+str(case_counter)+': '+calculate_candy_split(number_list))
  output_file_handle.write('Case #'+str(case_counter)+': '+calculate_candy_split(number_list)+'\n')

file_handle.close()
output_file_handle.close()
