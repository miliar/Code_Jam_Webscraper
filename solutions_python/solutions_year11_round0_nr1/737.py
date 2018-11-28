#!/usr/bin/python

import sys

fp = open(sys.argv[1], 'r')

num_cases = int(fp.readline())

for i in range(0, num_cases):
   line = fp.readline()
   words = line.split()

   blue_index = 1
   orange_index = 1
   blue_buttons = []
   orange_buttons = []
   buttons_to_press = []
   count = 0

   words.pop(0)

   while len(words) > 0:
      buttons_to_press.append((words[0], int(words[1])))
      if words[0] == 'B':
         blue_buttons.append(int(words[1]))
      else:
         orange_buttons.append(int(words[1]))
      words.pop(0)
      words.pop(0)

   while len(buttons_to_press) > 0:
      count += 1

      if buttons_to_press[0][0] == 'B':
         if blue_index == blue_buttons[0]:
            buttons_to_press.pop(0)
            blue_buttons.pop(0)
         else:
            if blue_index < blue_buttons[0]:
               blue_index += 1
            else:
               blue_index -= 1

         if len(orange_buttons) > 0:
            if orange_index != orange_buttons[0]:
               if orange_index < orange_buttons[0]:
                  orange_index += 1
               else:
                  orange_index -= 1

      else:
         if orange_index == orange_buttons[0]:
            buttons_to_press.pop(0)
            orange_buttons.pop(0)
         else:
            if orange_index < orange_buttons[0]:
               orange_index += 1
            else:
               orange_index -= 1

         if len(blue_buttons) > 0:
            if blue_index != blue_buttons[0]:
               if blue_index < blue_buttons[0]:
                  blue_index += 1
               else:
                  blue_index -= 1


   print "Case #" + str(i+1) + ": " + str(count)
