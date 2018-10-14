''' 
Tic-Tac-Toe-Tomek
Google Code Jam 2013 Challenge
Qualification Round
Lenny Khazan
'''

def result_for_case(case):
  # Check for horizontal win
  for line in case:
    curr_line = line.replace('T', 'X')
    if curr_line == 'XXXX':
      return 'X won'
    
    curr_line = line.replace('T', 'O')
    if curr_line == 'OOOO':
      return 'O won'
    
    # Generate column strings
    columns = []
    for column in range(4):
      curr_column = ''
      for line in range(4):
        curr_column += case[line][column]
      columns.append(curr_column)
    
    for column in columns:
      curr_column = column.replace('T', 'X')
      if curr_column == 'XXXX':
        return 'X won'
      
      curr_column = column.replace('T', 'O')
      if curr_column == 'OOOO':
        return 'O won'
    
    # Generate diagonal strings
    diagonals = ['', '']
    x = 0
    y = 0
    for i in range(4):
      diagonals[0] += case[x][y]
      diagonals[1] += case[abs(x - 3)][y]
      x += 1
      y += 1
    print diagonals
    
    for diagonal in diagonals:
      curr_diagonal = diagonal.replace('T', 'X')
      if curr_diagonal == 'XXXX':
        return 'X won'
      
      curr_diagonal = diagonal.replace('T', 'O')
      if curr_diagonal == 'OOOO':
        return 'O won'
      
    # Check unfinished
    for line in case:
      if line.find('.') != -1:
        return 'Game has not completed'
    
    return 'Draw'
        

def main():
  # Get the input
  input_path = 'Input/input.txt'
  output_path = 'output.txt'
  input_file = open(input_path, 'r')
  lines = input_file.readlines()
  case_count = int(lines[0])
  lines = lines[1:]
  cases = []
  while len(lines) > 1:
    case_lines = lines[0:4]
    for i in range(len(case_lines)):
      case_lines[i] = case_lines[i].replace('\n', '')
      
    cases.append(case_lines)
    lines = lines[5:]
  
  output = ''
  for i in range(len(cases)):
    output += 'Case #' + str(i + 1) + ': ' + result_for_case(cases[i]) + '\n'
  
  output_file = open(output_path, 'w+b')
  output_file.write(output)
  

if __name__ == '__main__':
  main()