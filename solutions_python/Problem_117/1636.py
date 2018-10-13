import math
import re
import sys

def main():

  lines = [x.strip() for x in sys.stdin.readlines()]

  num_cases = int(lines[0])
  line_num = 1
  
  for i in range (1,num_cases+1):
    #print lines[line_num]
    line = re.split("\D", lines[line_num])
    rows = int(line[0])
    cols = int(line[1])
    #print rows, cols, line_num
    lawn = lines[line_num+1:line_num+rows+1]
    lawn = [re.split("\D", line) for line in lawn]
    #print lawn
    line_num += rows+1

    lawn_validity = []

    result = True
    if rows > 1 and cols > 1:
      for row_num in range(0,rows):
        row_validity = []
        lawn_validity.append(row_validity)
        row = lawn[row_num]
        heighest_in_row = 0
        for col_num in range(0,cols):
          cell_validity = "N"
          cell = row[col_num]
          cell = int(cell)

          if cell < heighest_in_row:  
            # not valid by row
            if check_col(col_num, row_num, lawn, rows, cols) is False:
              result = False
              break
            else:
              cell_validity = "C"
          else:
            if cell > heighest_in_row:
              # If we update the highest, then any that thought they were safe are now not.
              heighest_in_row = cell 
              for j in range (0, len(row_validity)):
                if row_validity[j] is "R":
                  if check_col(j, row_num, lawn, rows, cols) is False:
                    result = False
                    break
                  else:
                    row_validity[j] = "C"
            cell_validity = "R"           
          row_validity.append(cell_validity)  

    
    if result is True:
      print "Case #"+str(i)+": YES"
    else: 
      print "Case #"+str(i)+": NO"
        
# return True if its the biggest in its column
def check_col(col_num, row_num, lawn, num_rows, num_cols):
  test = lawn[row_num][col_num]
  for i in range(0, num_rows):
    if lawn[i][col_num] > test:
      return False
  return True
    
if __name__ == "__main__":
  main()