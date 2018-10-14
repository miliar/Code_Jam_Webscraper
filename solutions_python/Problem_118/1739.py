''' 
Fair and Square
Google Code Jam 2013 Challenge
Qualification Round
Lenny Khazan
'''

import math

def fair_square(numb):
  string_numb = str(numb)
  reverse = string_numb[::-1]
  square_root = math.sqrt(numb)
  reverse_root = str(int(square_root))[::-1]
  if reverse == string_numb and str(int(square_root)) == reverse_root and square_root % 1 == 0:
    return True
  else:
    return False

def result_for_case(case):
  counter = 0
  for i in range(int(case[0]), int(case[1]) + 1):
    if fair_square(i):
      counter += 1
    
  return counter

def main():
  input_path = 'Input/input.txt'
  output_path = 'output.txt'
  input_file = open(input_path, 'r')
  lines = input_file.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '') # Get rid of annoying newlines
  
  case_count = int(lines[0])
  lines = lines[1:]
  
  cases = []
  for i in range(len(lines)):
    line_parts = lines[i].split(' ')
    for i in range(len(line_parts)):
      line_parts[i] = line_parts[i].replace(' ', '')
    
    cases.append(line_parts)
        
  output_string = ''
  for i in range(len(cases)):
    output_string += 'Case #' + str(i + 1) + ': ' + str(result_for_case(cases[i])) + '\n'
    
  output_file = open(output_path, 'w+b')
  output_file.write(output_string)

if __name__ == '__main__':
  main()