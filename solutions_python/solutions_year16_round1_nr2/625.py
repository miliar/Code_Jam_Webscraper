import os
import sys
  
def Main():
  result_list = []
  temp_result = []
  arg = []
  CASE_N = int(raw_input())
  for i in range(0, CASE_N) : 
    NUM = int(raw_input())

    line = raw_input()
    arg = line.split()    
    for tmp_arg in arg : 
      tmp_num = int(tmp_arg)
      temp_result.append(tmp_num)

    for j in range(0, (NUM - 1)*2) : 
      line = raw_input()
      arg = line.split()

      for tmp_arg in arg : 
        tmp_num = int(tmp_arg)
        remove_num = 0       
        for result_num in temp_result :
          if(tmp_num == result_num) :
            remove_num = tmp_num
            break
        if(remove_num == 0) : 
          temp_result.append(tmp_num)
        else :
          temp_result.remove(remove_num)
    temp_result.sort()
    result_list.append(temp_result)
    temp_result = []
  count = 1
  for result in result_list :
    sys.stdout.write('Case #' + str(count) + ':')

    for result_one in result :
      sys.stdout.write(' ' + str(result_one))
    sys.stdout.write('\n')
    count = count + 1

if __name__ == '__main__':
  sys.exit(Main())