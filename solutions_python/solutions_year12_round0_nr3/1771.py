from collections import deque
import sys
import string

for index,line in enumerate(open(sys.argv[1])):
  if index != 0:
    number_list = line.split(" ")
    counter = 0
    lower = int(number_list[0])
    upper = int(number_list[1])
    for number in range(lower,upper):
      a = str(number)
      dq = deque(a)
      for j in range(0,len(dq)):
        b = ""
        dq.rotate(1);
        for k in dq:
          b = b+k
#    print a+" - "+b
        if number >= lower and number < int(b) and int(b) <= upper:
          counter = counter + 1
#      print a+" - "+b
    print "Case #"+str(index)+": "+str(counter)
