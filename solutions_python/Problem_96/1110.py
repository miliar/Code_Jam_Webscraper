try:
    import psyco
    psyco.full()
except:
    pass

from sys import stdin, stdout

n = int(stdin.readline())

for case in range(n):
   input_list = map(int,stdin.readline().split())
   googlers = input_list[0]
   remaining_surprises = input_list[1]
   desired_result = input_list[2]  
   results = input_list[3:]
   best_googlers = 0   

   for result in results:
      if result/3 >= desired_result:
         best_googlers += 1

      elif result == 0 or result/3 < desired_result - 2:
         continue

      else:
         scores = [desired_result]
         if result - desired_result % 2 == 0:
            scores.append((result - desired_result)/2)
            scores.append((result - desired_result)/2)

            if scores[1] >= scores[0] - 2:
               if scores[1] == scores[0] - 2:
                  if remaining_surprises:
                     remaining_surprises -= 1
                     best_googlers += 1
               else:
                  best_googlers += 1
         else:
            scores.append((result - desired_result)/2)
            scores.append((result - desired_result)/2 + 1)
            
            if scores[1] >= scores[0] - 2:
               if scores[1] == scores[0] - 2:
                  if remaining_surprises:
                     remaining_surprises -= 1
                     best_googlers += 1
               else:
                  best_googlers += 1

   output_str = "Case #%d: " % (case + 1)
   output_str += str(best_googlers)   
   stdout.write(output_str + '\n');
