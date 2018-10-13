'''
Created on Apr 11, 2015

@author: JuanFMx2
'''
import sys
import os.path
import traceback


class Quaternion( object ):
  
  def __init__(self,str_quat,negative=False):
    self.str_quat = str_quat
    self.negative = negative
  
  def __str__(self):
    if self.negative:
      return '-'+self.str_quat
    return self.str_quat

  @staticmethod
  def get_quat_from_ijk_char(ijk_val):
    return Quaternion.ijk_access[ijk_val]
  
  def negate(self):
    return Quaternion.neg_access[self]
  
  def multiply(self,next_quat):
    neg = self.negative != next_quat.negative
    res = Quaternion.calc_matrix[self.str_quat][next_quat.str_quat]
    if neg:
      return Quaternion.neg_access[res]
    return res
  
  def is_i(self):
    return self == Quaternion.q_i
  
  def is_j(self):
    return self == Quaternion.q_j
  
  def is_k(self):
    return self == Quaternion.q_k
  
  def is_1(self):
    return self == Quaternion.q_1
  
  def is_1_m(self):
    return self == Quaternion.q_1_m
  
# Quaternion constants
Quaternion.q_1 = Quaternion('1')
Quaternion.q_i = Quaternion('i')
Quaternion.q_j = Quaternion('j')
Quaternion.q_k = Quaternion('k')
Quaternion.q_1_m = Quaternion('1',True)
Quaternion.q_i_m = Quaternion('i',True)
Quaternion.q_j_m = Quaternion('j',True)
Quaternion.q_k_m = Quaternion('k',True)
  
Quaternion.neg_access = {
                            Quaternion.q_1:Quaternion.q_1_m,
                            Quaternion.q_i:Quaternion.q_i_m,
                            Quaternion.q_j:Quaternion.q_j_m,
                            Quaternion.q_k:Quaternion.q_k_m,
                            
                            Quaternion.q_1_m:Quaternion.q_1,
                            Quaternion.q_i_m:Quaternion.q_i,
                            Quaternion.q_j_m:Quaternion.q_j,
                            Quaternion.q_k_m:Quaternion.q_k,
                            }
  
Quaternion.quat_vals = ['1','i','j','k']
  
Quaternion.ijk_access = {
                            'i':Quaternion.q_i,
                            'j':Quaternion.q_j,
                            'k':Quaternion.q_k
                            }
  
Quaternion.calc_matrix = {
                             '1':{
                                  '1':Quaternion.q_1,
                                  'i':Quaternion.q_i,
                                  'j':Quaternion.q_j,
                                  'k':Quaternion.q_k
                                  },
                             'i':{
                                  '1':Quaternion.q_i,
                                  'i':Quaternion.q_1_m,
                                  'j':Quaternion.q_k,
                                  'k':Quaternion.q_j_m
                                  },
                             'j':{
                                  '1':Quaternion.q_j,
                                  'i':Quaternion.q_k_m,
                                  'j':Quaternion.q_1_m,
                                  'k':Quaternion.q_i
                                  },
                             'k':{
                                  '1':Quaternion.q_k,
                                  'i':Quaternion.q_j,
                                  'j':Quaternion.q_i_m,
                                  'k':Quaternion.q_1_m
                                  },
                             }

def dijkstra(case_num,line_input_1,line_input_2):
  try:
    parts = line_input_1.split()
    line_input_2 = line_input_2.strip()
    num_chars = long(parts[0])
    num_reps = long(parts[1])
    found_i = False
    found_j = False
    cur_rep = 0
    cur_q_val = None
    invalid = False
    while cur_rep < num_reps:
      for char_i in line_input_2:
        next_q = Quaternion.get_quat_from_ijk_char(char_i)
        if cur_q_val is None:
          cur_q_val = next_q
        else:
          cur_q_val = cur_q_val.multiply(next_q)
        
        if not found_i and cur_q_val.is_i():
          found_i = True
        # is evaluated with is_k because ij = k and and i should have been found
        # before searching for a k
        if found_i and not found_j and cur_q_val.is_k():
          found_j = True
        if cur_rep > 0 and found_i and found_j:
          break
      
      # The first iteration over the string will check if the total string
      # will ever reduce to -1 since ijk = -1
      if cur_rep == 0:
        reduces_to_1_m = True
        if cur_q_val.is_1():
          reduces_to_1_m = False
        elif cur_q_val.is_1_m():
          reduces_to_1_m = (num_reps%2)==1
        else:
          reduces_to_1_m = ((num_reps-2)%4) == 0
          
        if not reduces_to_1_m:
          invalid = True
          break
      cur_rep += 1
    if invalid:
      answer = "NO"
    elif found_i and found_j:
      answer = "YES"
    else:
      answer = "NO"
  except:
    traceback.print_exc()
    print "Error parsing line \n%s\n%s"%(line_input_1,line_input_2)
    sys.exit(0)
  print "Case #%s: %s"%(case_num,answer)

def parse_input(input_path, process_test_case_func):
  with open(input_path) as f:
    cur_line = f.readline()
    try:
      num_lines_to_process = int(cur_line)
    except:
      print "'%s' is not a number!" % cur_line
      sys.exit(0)
    
    for i in range(num_lines_to_process):
      line_1 = f.readline()
      if not cur_line:
        print "line %s is empty!" % cur_line
        sys.exit(0)
      line_2 = f.readline()
      if not cur_line:
        print "line %s is empty!" % cur_line
        sys.exit(0)
      process_test_case_func((i+1),line_1,line_2)
    content = f.readlines()

def main(input_path):
  if os.path.isfile(input_path):
    parse_input(input_path,dijkstra)
  else:
    print "Unknown file: '%s'" % input_path
    sys.exit(0)
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    main(sys.argv[1])
  else:
    print "Insufficient Parameters"
    sys.exit(0)