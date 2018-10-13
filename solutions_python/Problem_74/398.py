import sys

def strategy(robot, button) :
   po = 1
   pb = 1
   tasks = len(robot)
   result = 0
   i = 0
   t = 0
   while i < tasks :
      if robot[i] == 'O' :
         t -= abs(po - button[i])
	 po = button[i]
	 if t >= 0 :
	    t = 1
	 else :
	    t = 1 - t
	 i += 1
	 while i < tasks and robot[i] == 'O' :
	    t += 1 + abs(po - button[i])
	    po = button[i]
	    i += 1
	 result += t
      elif robot[i] == 'B' :
         t -= abs(pb - button[i])
	 pb = button[i]
	 if t >= 0 :
	    t = 1
	 else :
	    t = 1 - t
	 i += 1
         while i < tasks and robot[i] == 'B' :
	    t += 1 + abs(pb - button[i])
	    pb = button[i]
	    i += 1
	 result += t
   return result


if __name__ == '__main__' :
   tests = int(sys.stdin.readline())
   i = 1
   while i <= tests :
      line = sys.stdin.readline()
      arr = line.split()
      robot = arr[1::2]
      button = [int(x) for x in arr[2::2]]
      result = strategy(robot, button)
      print 'Case #%d: %d' % (i, result)
      i += 1
