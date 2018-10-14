
import sys
import math

def is_palindrome(s):
  if s == '':
      return True
  if s[0] == s[-1]:
      return is_palindrome(s[1:-1])
  return False
  
def get_amount(line):
  intvl = line.split()
  for i in range(2):
    intvl[i] = int(intvl[i])
  result = 0
  bottom = int(math.ceil(math.sqrt(intvl[0])))
  top = int(math.sqrt(intvl[1]))
  for i in range(bottom, top + 1):
     result += 1 if (is_palindrome(str(i)) and is_palindrome(str(i ** 2))) else 0
  return result
  
def main():
  input = open(sys.argv[1], 'r') # read only
  # will need input.readlines(), input.read(), or something similar later, which will separate lines into
  # list elements, leaving the \n attached to the end of each line
  # the string method .rstrip('\n') will remove these
  output = open(sys.argv[2] + '.out', 'w') # write new file
  # will use output.write(result + '\n') later to write one 'result' line at a time to the output file
  lines = input.readlines()
  #lines.pop()
  lines.pop(0)
  input.close()
  case = 1
  for line in lines:
    output_line = 'Case #{}: {}'.format(case, get_amount(line))
    output.write(output_line + '\n')
    case += 1
  # at end, close files to prevent any strange behavior due to file being left open after program closes
  output.close()
  print 'Done!'
  
if __name__ == '__main__':
  main()