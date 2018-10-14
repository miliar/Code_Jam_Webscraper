import sys

isprint = False 
#isprint = True 
def comment(t):
  if(isprint): print t

if __name__ == '__main__':
  data = open(sys.argv[1])
  n_case = int(data.readline().strip())
  for n in xrange(1,n_case+1):
    q_array = data.readline().strip().split() 
    orders = []
    for i in xrange(1,len(q_array),2):
      orders.append((q_array[i],int(q_array[i+1]))) 
    
    pos_o = 1
    pos_b = 1
    t_o = 0
    t_b = 0
    prev_order = None
    while orders != []:
      robot,button = orders[0]
      orders = orders[1:]
      if robot == 'O':
        if button > pos_o : t_o += button - pos_o + 1 
        else: t_o += pos_o - button +1 
        comment("t at o :" + str(abs(button - pos_o + 1))) 
        pos_o = button
        if t_b >= t_o and prev_order == 'B':
          t_o = t_b + 1
        prev_order = 'O'  
      elif robot == 'B': 
        if button > pos_b : t_b += button - pos_b + 1 
        else: t_b += pos_b - button + 1 
        comment("t at b :" + str(abs(button - pos_b + 1))) 
        pos_b = button
        if t_o >= t_b and prev_order == 'O':
          t_b = t_o + 1
        prev_order = 'B'  
      
      comment('t_o :' + str(t_o))
      comment('t_b :' + str(t_b))
      #raw_input()
    
    print "Case #%d: %d"%(n,max(t_o,t_b))

