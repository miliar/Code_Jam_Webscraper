def main ():
  input = open('B-large.in', 'r')
  data = input.read().split('\n')
  num_cases = int(data.pop(0))
  result = ''
  for index,case in enumerate(data):
    if case == '':
      break
    scores = case.split(' ')
    num_scores = scores.pop(0)
    count = 0
    surprises = int(scores.pop(0))
    min_result = int(scores.pop(0))
    min_sum = 0
    for score in scores:
      if min_result > 1:
        min_sum = min_result * 3 - 4
        #print str(min_sum) + str(score)
      elif min_result == 1:
        min_sum = 1
        #print str(min_sum) + str(score)
      else:
        min_sum = 0
        #print str(min_sum) + str(score)
      if int(score) > (min_result * 3) - 3:
        count += 1
        #print 'plus one'
      elif int(score) >= min_sum and surprises > 0:
        count += 1
        surprises -= 1
        #print 'plus one with surprise'
    result += 'Case #' + str(index+1) + ': ' + str(count)
    result += '\n'

  output = open('output.txt', 'w')
  output.write(result)
    
  
if __name__ == '__main__':
  main()