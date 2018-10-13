import sys
from pprint import pprint

def get_num_input():
  num = sys.stdin.readline()
  try:
    num = int(num)
  except ValueError:
    print("Error : first line of input is not an int")
    exit()
  return num

def line_to_item(line):
  if line[-1] == '\n':
    return line[:-1]  #remove trailing '\n'
  else:
    return line

def is_tidy(num):
  for i in range(1, len(num)):
    if not (int(num[i]) >= int(num[i-1])):
      return False
  return True

def get_last_non_9_index(item):
  i = len(item)-1
  while True:
    if item[i] != '9':
      return i
    if i == 0:
      print("All is already 9")
      exit()
    i -= 1

def compute(item):
  while(not is_tidy(item)):
    #get the last digit which is not a 9
    i = get_last_non_9_index(item)

    last_non_9_digit = int(item[i])       #get the digit as a number
    multiple = 10**(len(item) - i - 1)    #weight of that digit

    #substract the needed amount so that the last non 9 digit and all
    #following digits are 9's
    item = str(int(item) - (last_non_9_digit + 1) * multiple)
  return item
      

def main():
  num = get_num_input()

  #MAIN LOOP
  i = 0
  for line in sys.stdin:
    i += 1
    print("Case #" + str(i) + ": ", end='')
    item = line_to_item(line)
    print(compute(item))

main()

