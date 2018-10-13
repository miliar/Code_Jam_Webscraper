#!/usr/bin/python

def opposing_exists(needle, haystack):
    if haystack and (needle == haystack[0] or needle == haystack[1]): return True
    return False

def should_clear(needle, opposing, haystack):
    if len(opposing) == 0: return False
    if len(opposing) == 1 and needle == haystack[opposing[-1]]: return False
    for i in range(len(opposing)):
       if needle != haystack[opposing[i]]: return True

    return False

def solve():
   combined = None
   opposed = None
   opposing = []

   data  = raw_input().split()

   c = int(data[0])
   next = 1

   if c > 0: 
      combined = data[next]
      next = 2

   d = int(data[next])
   if d > 0:
      opposed = data[next+1]
      next += 1
   
   next += 1

   n = int(data[next])
   string = data[next+1]
   output = []
   output.append(string[0])

   if opposing_exists(string[0], opposed): opposing.append(0)

   for i in range(1, n):
      #print opposing
      output.append(string[i])
      #print output

      current = len(output) - 1
      if combined:
         letters = combined[:-1]
         if letters == ''.join(output[-2:]) or letters[::-1] == ''.join(output[-2:]):
            output = output[:-2]
            output.append(combined[-1])
            if current-1 in opposing: opposing.remove(current-1)
            continue

      if opposing_exists(string[i], opposed):
         if should_clear(string[i], opposing, output):
            output = []
            opposing = []
         else: opposing.append(current)
      
   return '[%s]' % ', '.join(map(str, output))
          
for i in range(input()):
    print "Case #%d: %s" % (i+1, solve())
    
    
