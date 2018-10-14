# Dancing with googlers
# Google codejam - 14 April 2012

from itertools import combinations_with_replacement, product

def is_surprising(triplet):
   a, b, c = triplet
   return (abs(a-b) == 2 or abs(a-c) == 2 or abs(b-c) == 2)

def count_surprising(choice):
   count = 0
   for triplet in choice:
      if is_surprising(triplet):
         count += 1
   return count

def least_best_result_count(choice, least_best_result):
   count = 0
   for triplet in choice:
      a, b, c = triplet
      if (a >= least_best_result or b >= least_best_result or c >= least_best_result):
         count += 1
   return count
   
def get_possible_scores(total_score):
   score_list = []
   c = combinations_with_replacement(range(0,11), 3)
   for score_triplet in c:
      if sum(score_triplet) == total_score:
         a, b, c = score_triplet
         if abs(a-b) <= 2 and abs(a-c) <= 2 and abs(b-c) <= 2:
            score_list.append(score_triplet)
   return score_list

def get_input(filename):
   file = open(filename,'r')
   lines = [line.strip() for line in file.readlines()]
   file.close()
   return lines

def solve_line(googlers_count, surprising_count, least_best_result, total_points):
   
   #print "G = %d | S = %d | p = %d" % (googlers_count, surprising_count, least_best_result)
   #print "points = %s" % ', '.join(map(lambda n: str(n), total_points))
   
   possibilities = []
   for point in total_points:
      possible_scores = get_possible_scores(point)
      #print "score: %d -> %s" % (point, possible_scores)
      possibilities.append(possible_scores)
   
   p = product(*possibilities)
   
   max_googlers = []
   for choice in p:
      #print choice,
      #print "(%d surprising)" % count_surprising(choice)
      if count_surprising(choice) == surprising_count:
         max_googlers_this_choice = least_best_result_count(choice, least_best_result)
         max_googlers.append(max_googlers_this_choice)
   
   if max_googlers:
      return max(max_googlers)
   
input_lines = get_input("B:\\Downloads\\B-small-attempt0.in")

number_of_test_cases = int(input_lines[0])

i = 1
for line in input_lines[1:]:
   line = line.split()
   line = map(lambda number: int(number), line)
   googlers_count = line[0]
   surprising_count = line[1]
   least_best_result = line[2]
   total_points = line[3:]
   
   answer = solve_line(googlers_count, surprising_count, least_best_result, total_points)
   print "Case #%d: %d" % (i, answer)
   i += 1