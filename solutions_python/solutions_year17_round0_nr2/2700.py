def calculate(n):
    answer = n
    target = n
    last_index = -1
    is_answer = False
    while is_answer != True:
        target_str = list(str(target))
        is_answer = True
        for j in range(len(target_str)-1):
            if target_str[j] > target_str[j+1]:
                is_answer = False
                if target_str[j] == '0':
                    target_str[j] = '9'
                else:
                    target_str[j] = str(int(target_str[j]) - 1)
                for k in range(len(target_str[j+1:])):
                    target_str[j+k+1] = '9'
                    target = long(''.join(target_str))
                break
        
        if is_answer == True:
            answer = target
            break

    return answer

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  n = int(raw_input())  # read a list of integers, 2 in this case
  print "Case #{}: {}".format(i, calculate(n))
  # check out .format's specification for more formatting options
