# -*- coding: utf-8 -*-

def flip(sk):
    if sk =='-':
        s_flip = '+'
    if sk =='+':
        s_flip= '-'
    return s_flip
    
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for ii in xrange(1, t + 1):
  s, ka_i = [(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #print "Case #{}: {} {}".format(i, n + m, n * m)
  # check out .format's specification for more formatting options
  ka_i = int(ka_i)
  s_len = len(s)
  sl = list(s)

  temp = []
#for i in range(0,s_len+1-ka_i,ka_i):
#    temp = sl[i:i+ka_i]
#    update,count = pattern(temp)
#    sl[i:i+ka_i]= update # 1st round

  counter = 0
  if sl == ['+']*s_len:
     counter = 0
  for i in range(0,s_len+1-ka_i):
    
    if sl[i] == '-':
        t_l = []
        for item in sl[i:i+ka_i]:
            item_temp = flip(item)
            t_l.append(item_temp)
        sl[i:i+ka_i] = t_l
        i = i+ka_i
        counter = counter +1

  if sl !=['+']*s_len:
     result = 'IMPOSSIBLE'
  else :
     result = counter 
  print "Case #{}: {}".format(ii, result)             
    


