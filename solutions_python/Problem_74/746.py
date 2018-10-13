test_cases = int(raw_input())
for test_case in xrange(test_cases):
   orange_pos = 1
   orange_buttons = []

   blue_pos = 1
   blue_buttons = []

   time_taken = 0
   button_index = 1

   mastermind = raw_input().split(' ')
   buttons = mastermind[1:]
   num_steps = buttons[0]
   for i in xrange(0, len(buttons), 2):
      if buttons[i] == 'B':
         blue_buttons.append((int(buttons[i + 1]), (i + 2)/2))
      else:
         orange_buttons.append((int(buttons[i + 1]), (i + 2)/2))

   while len(orange_buttons) > 0 or len(blue_buttons) > 0:
      time_taken += 1
      #print "second",time_taken
      pushed = 0
      if len(orange_buttons) > 0:
         if orange_pos == orange_buttons[0][0]:
            if button_index == orange_buttons[0][1]:
               orange_buttons.pop(0)
               pushed = 1
               #print "orange pushing"
            else:
               #print "orange waiting", orange_buttons[0][0]
               pass # wait
         else:
            if orange_pos < orange_buttons[0][0]:
               #print "orange moving up"
               orange_pos += 1
            else:
               #print "orange moving down"
               orange_pos -= 1
            
      if len(blue_buttons) > 0:
         if blue_pos == blue_buttons[0][0]:
            if button_index == blue_buttons[0][1]:
               blue_buttons.pop(0)
               pushed = 1
               #print "blue pushing"
            else:
               pass # wait
               #print "blue waiting"
         else:
            if blue_pos < blue_buttons[0][0]:
               #print "blue moving up"
               blue_pos += 1
            else:
               #print "blue moving down"
               blue_pos -= 1
      if pushed == 1:
         button_index += 1 # push the button
         
   print "Case #" + str(test_case + 1) + ":", time_taken
