import sets

def str_to_set(s):
   return sets.Set(s.split(" "))

def read_arrangement():
   row = int(raw_input());
   for r in range(1, 5):
      if r == row:
         candidates = str_to_set(raw_input())
      else:
         raw_input() 
   return candidates
   

nb_ins = int(raw_input());
for x in range(0, nb_ins):
   candidates = read_arrangement();
   candidates &= read_arrangement();
   if len(candidates) == 0:
      result = "Volunteer cheated!"
   elif len(candidates) > 1:
      result = "Bad magician!"
   else:
      result = candidates.pop()
   print "Case #" + str(x + 1) + ": " + result 

