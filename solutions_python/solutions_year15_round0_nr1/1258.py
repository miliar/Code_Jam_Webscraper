'''
Created on Apr 10, 2015

@author: JuanFMx2
'''
import sys
import os.path
import traceback


shyness_orig = []

def parse_standing_vation_line(line_input):
  pass

def standing_ovation(case_num,line_input):
  answer = 0
  parts = line_input.split()
  try:
    cur_aud_applausing = 0
    s_max = int(parts[0])
    cur_s = 0
    for char_digit in parts[1]:
      cur_aud_num = int(char_digit)
      if cur_aud_applausing < cur_s:
        aud_dif = cur_s-cur_aud_applausing
        cur_aud_applausing += aud_dif
        answer += aud_dif
      cur_aud_applausing += cur_aud_num
      cur_s += 1
      if cur_aud_applausing >= s_max:
        break
  except:
    traceback.print_exc()
    print "Error parsing line '%s'"%line_input
    sys.exit()
  print "Case #%s: %s"%(case_num,answer)

def parse_input(input_path, process_line_func):
  with open(input_path) as f:
    cur_line = f.readline()
    try:
      num_lines_to_process = int(cur_line)
    except:
      print "'%s' is not a number!" % cur_line
      sys.exit(0)
    
    for i in range(num_lines_to_process):
      cur_line = f.readline()
      if not cur_line:
        print "line %s is empty!" % cur_line
        sys.exit(0)
      process_line_func((i+1),cur_line)
    content = f.readlines()
    

def main(input_path):
  if os.path.isfile(input_path):
    parse_input(input_path, standing_ovation)
  else:
    print "Unknown file: '%s'" % input_path
    sys.exit(0)
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    main(sys.argv[1])
  else:
    print "Insufficient Parameters"
    sys.exit(0)