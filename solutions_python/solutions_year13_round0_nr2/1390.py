''' 
Lawnmower
Google Code Jam 2013 Challenge
Qualification Round
Lenny Khazan
'''

def result_for_case(case):
  
  ideal_case = case # The ideal case that we want to reach (case will be modified later, so store a copy here)
  
  temp_case = [ ]
  ideal_case = [ ]
  
  for row in range(len(case)):
    temp_case.append( [] )
    ideal_case.append( [] )
    split_row = case[row].split(' ')
    for column in range(len(split_row)):
      ideal_case[row].append(int(split_row[column]))
      temp_case[row].append(100)
    
  case = temp_case
    
  # cut each row as much as possible
  for i in range(len(ideal_case)):
    max_height = 1 # The tallest grass that is in this row
    for val in ideal_case[i]:
      if val > max_height:
        max_height = val
      
    for j in range(len(case[i])):
      if case[i][j] > max_height:
        case[i][j] = max_height
        
    # cut each column as much as possible
  for i in range(len(ideal_case[0])):
    max_height = 1 # The tallest grass that is in this row
    for j in range(len(ideal_case)):
      if ideal_case[j][i] > max_height:
        max_height = ideal_case[j][i]
    
    for j in range(len(case)):
      if case[j][i] > max_height:
        case[j][i] = max_height
  
  if case == ideal_case:
    return 'YES'
  else:
    return 'NO'

def main():
  input_path = 'Input/input.txt'
  output_path = 'output.txt'
  
  input_file = open(input_path, 'r')
  lines = input_file.readlines()
  for i in range(2, len(lines)):
    lines[i] = lines[i].replace('\n', '') # Get rid of annoying newlines
  case_count = int(lines[0])
  lines = lines[1:]
  cases = []
  for i in range(case_count):
    case_lines = int(lines[0].split(' ')[0])
    lines = lines[1:]
    cases.append(lines[:case_lines])
    lines = lines[case_lines:]
  
  output_string = ''
  for i in range(len(cases)):
    output_string += 'Case #' + str(i + 1) + ': ' + result_for_case(cases[i]) + '\n'
  
  output_file = open(output_path, 'w+b')
  output_file.write(output_string)

if __name__ == '__main__':
  main()