import sys

num_tests = int(raw_input())
for i in range(num_tests):
   args = map(float, raw_input().split(' '))
   start_rate = 2.0
   cur_rate = 2.0
   cur_time = 0
   prev_time = cur_time
   done = False

   while not done:
      cur_time = 0
      temp_rate = start_rate
      while temp_rate <= cur_rate:
         if temp_rate < cur_rate:
            cur_time += args[0] / temp_rate
         else:
            cur_time += args[2] / temp_rate
         temp_rate += args[1]
      if prev_time > 0 and cur_time > prev_time:
         done = True
      else:
         prev_time = cur_time
         cur_rate += args[1]

   print 'Case #' + str(i+1) + ': ' + '{0:.7f}'.format(prev_time)




