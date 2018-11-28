import sys
import getopt

case = "Case #"
on =   ": ON\n"
off =  ": OFF\n"

input_name = "A-large.in"
output_name = "A-large.out"

def run_case(case_string, output_list, case_num):
  case_list = case_string.split(" ")
  N = int(case_list[0])
  K = int(case_list[1])
  
  works = False
  
  base_n = 2**N
  
  K = K % base_n
  
  if K == base_n - 1:
    works = True
  
  result = on if works else off
  output_list.append(case + str(case_num + 1) + result)

def main():
  input_file = open(input_name, "r")
  output_file = open(output_name, "w")
  output_list = []
  
  first = True
  num_cases = 0
  current_case = 0
  cases = {-1:""}
  for line in input_file:
    if first: #get number of cases
      num_cases = int(line)
      first = False
    else: # get all cases and store them in cases dic
      if current_case < num_cases:
        cases[current_case] = line
        current_case = current_case + 1
      else:
        break
  
  #run each case
  i = 0
  while i < num_cases:
    run_case(cases[i], output_list, i)
    i = i + 1
  
  output_file.writelines(output_list)
  #clean up
  input_file.close()
  output_file.close()

if __name__ == "__main__":
  main()

