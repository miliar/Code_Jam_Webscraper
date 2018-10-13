import sys

input = sys.stdin

N = int(input.readline())
for n in xrange(1,N+1):
  data = input.readline().strip().split(' ')[1:]
  data_list = zip(\
      [e for i,e in enumerate(data) if i%2 == 0], \
      [int(e) for i,e in enumerate(data) if i%2 == 1])

  times = [0] * len(data_list) 
  times[0] = data_list[0][1] - 1 + 1
 
  for i in xrange(1, len(data_list)):
    curr_type, curr_index = data_list[i]
    pre_type, pre_index = data_list[i-1]

    #print times

    if curr_type == pre_type:
      times[i] = times[i-1] + abs(curr_index - pre_index) + 1
    else:
      recent_prev_index = 1
      recent_prev_time = 0
      for j in xrange(i-1, -1, -1):
        p_type, p_index = data_list[j]
        if p_type == curr_type:
          recent_prev_index = p_index
          recent_prev_time = times[j]
          break
      
      diff = curr_index - recent_prev_index if curr_index > recent_prev_index else recent_prev_index - curr_index
      #print 'diff=%d,times=%d'%(diff,times[-1])
      if diff + recent_prev_time > times[i-1]:
        times[i] = diff + recent_prev_time + 1
      else:
        times[i] = times[i-1] + 1
  print 'Case #%d: %d'%(n, times[-1])
