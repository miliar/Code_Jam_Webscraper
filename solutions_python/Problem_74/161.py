f = open('A-large.in', 'r')
#f = open('A-small-attempt0.in', 'r')
#f = open('A-small.in', 'r')
out = open('A-small.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
  raw = f.readline().strip().split(' ')
  N = int(raw[0])
  test = raw[1:]
  
  orange_seq = []
  blue_seq = []
  
  for i in xrange(N):
    bot = test[2 * i]
    button = int(test[2 * i + 1])
    
    if bot == 'O':
      orange_seq.append((i, button))
    else:
      blue_seq.append((i, button))
  orange_seq.append((N, 101))
  blue_seq.append((N, 101))
  
  #print orange_seq, blue_seq
  
  o_pos = 1
  b_pos = 1
  buttons_pressed = 0
  time = 0
  
  while buttons_pressed < N:
    if orange_seq[0][0] < blue_seq[0][0]:
      if o_pos == orange_seq[0][1]:
        buttons_pressed += 1
        orange_seq = orange_seq[1:]
      elif o_pos < orange_seq[0][1]:
        o_pos += 1
      else:
        o_pos -= 1
      
      if b_pos < blue_seq[0][1]:
        b_pos += 1
      elif b_pos > blue_seq[0][1]:
        b_pos -= 1
    else:
      if b_pos == blue_seq[0][1]:
        buttons_pressed += 1
        blue_seq = blue_seq[1:]
      elif b_pos < blue_seq[0][1]:
        b_pos += 1
      else:
        b_pos -= 1
      
      if o_pos < orange_seq[0][1]:
        o_pos += 1
      elif o_pos > orange_seq[0][1]:
        o_pos -= 1
    time += 1
    
  print 'Case #%d: ' % (t + 1) + str(time)
  out.write('Case #%d: ' % (t + 1) + str(time) + '\n')
  

f.close()
out.close()
