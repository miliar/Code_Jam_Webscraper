#!/usr/bin/python -tt
import sys
## This function takes a number and the number system of that number
## and converts it into decimal number

no_of_test_case=0
test_case=[]
output=[]

def read_file(input_file):
  global no_of_test_case
  global test_case
  first=True
  local_test_case=''
  f=open(input_file,'rU')
  lines = [line.strip() for line in f]
  for line in lines:
    if first:
      no_of_test_case_str=line
      no_of_test_case=int(no_of_test_case_str)
      first=False
    else:
      if len(local_test_case)==16:
        test_case.append(local_test_case)
        local_test_case=''
      else:
        local_test_case=local_test_case+line
  f.close()
  test_case.append(local_test_case)
  
def write_file(out_file):
  global output
  f=open(out_file,'w')
  for i in range(len(output)):
    str="Case #%d: %s\n" %(i+1,output[i])
    f.write(str)
  f.close() 

def status(string):
  game_status=''
  empty=string.find('.')
  if empty <> -1:
    game_status='Game has not completed'
  else:
    X=string.find('X')
    O=string.find('O')
    if X==-1:
      game_status='O won'
    elif O==-1:
      game_status='X won'
    else: 
      game_status='Draw'
  return game_status

def splitter(tic_tac):
  for i in range(4):
    j= 4*i
    string = tic_tac[j:j+4]
    game_status = status(string)
    if game_status=='X won' or game_status=='O won':
      break
    
  if game_status=='Draw' or game_status=='Game has not completed':
    for i in range(4):
      string = tic_tac[i::4]
      game_status = status(string)
      if game_status=='X won' or game_status=='O won':
        break
  
  if game_status=='Draw' or game_status=='Game has not completed':
    string = tic_tac[0::5]
    game_status = status(string)
    if game_status=='Draw' or game_status=='Game has not completed':
      string = tic_tac[3::3]
      string = string[0:-1]
      game_status = status(string)     
  
  if game_status=='Draw' or game_status=='Game has not completed':
    empty=tic_tac.find('.')
    if empty==-1:
      game_status='Draw'
    else:
      game_status='Game has not completed'
  return game_status
  
def main():
  input_file='input.txt'
  output_file='output.txt'
  read_file(input_file)
  game_status=''
  global no_of_test_cases
  global test_case
  global output
  for i in range(no_of_test_case):
    game_status=splitter(test_case[i])
    output.append(game_status)  
  write_file(output_file)
if __name__=='__main__':
  main()

    