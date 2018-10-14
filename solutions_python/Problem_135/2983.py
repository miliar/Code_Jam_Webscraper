import sys

def MagicTrick(filename):
  f = open(filename)
  case_amount= int(f.readline())
  for case_number in range(case_amount):
    process_case(case_number, f)

	
def process_case(case_number, f):
  first_answer= int(f.readline())
  for i in range(first_answer-1):
    f.readline()
  line = f.readline()
  first_guess=set(line.split())
  for i in range(first_answer,4):
    f.readline()

  second_answer= int(f.readline())
  for i in range(second_answer-1):
    f.readline()
  second_guess=set(f.readline().split())
  for i in range(second_answer,4):
    f.readline()
  
  result = first_guess.intersection(second_guess)
  result_len = len(result)
  if result_len <1:
    print "Case #%d: Volunteer cheated!" % (case_number+1)
  elif result_len>1:
    print "Case #%d: Bad magician!" % (case_number+1)
  else:
    print "Case #%d: %s" % (case_number+1, result.pop())
 

def cc(C,F,T):
  factory_time=0.0
  current_productivity=2.0
  cookie_time=T/current_productivity  
  total_time = factory_time+cookie_time
  pre_total_time = total_time
  while total_time <=pre_total_time:
    factory_time+=(C/current_productivity)
    current_productivity+=F
    cookie_time=T/current_productivity
    pre_total_time=total_time
    total_time=factory_time+cookie_time
  return pre_total_time
  
if __name__ == "__main__":
  MagicTrick("input.txt")