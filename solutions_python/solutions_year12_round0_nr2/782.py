import sys



def is_possible(triplet):
  return max(triplet) - min(triplet) <= 2

def is_surprising(triplet):
  return max(triplet) - min(triplet) == 2
  
def score(triplet): 
  return sum(triplet)
  
def best_result(triplet):
  return max(triplet)

def build_legal_triplets():
  legal_triplets = {}
  for i in range(31):
    legal_triplets[i] = []
  for a in range(11):
    for b in range(a, 11):
      for c in range(b, 11):
        triplet = [a, b, c]
        if (is_possible(triplet)):
          triplet_score = score(triplet)
          legal_triplets[triplet_score].append(triplet)  
  return legal_triplets
  
def build_triplet_sets_for_scores(scores, legal_triplets):
  result = []
  for score in (scores):
    result.append(legal_triplets[score])
  return result

def get_result(triplet_sets, target_surprising, p):
  if (len(triplet_sets) == 0):
    return -1
  if (target_surprising > len(triplet_sets)):
    return -1
  my_triplets = triplet_sets[0]
  remaining_triplets = triplet_sets[1:]
  calculated_subresults = {}
  biggest_number = -1
  for triplet in (my_triplets):
    surprising_left = target_surprising
    if (is_surprising(triplet)):
      surprising_left = surprising_left - 1
    if (surprising_left < 0):
      continue
    subresult = 0
    if (len(remaining_triplets) > 0):
      subresult = calculated_subresults.get(surprising_left) or get_result(remaining_triplets, surprising_left, p)
      calculated_subresults[surprising_left] = subresult
    result = subresult
    if (subresult == -1):
      continue
    if (best_result(triplet) >= p):
      result = result + 1
    biggest_number = max(biggest_number, result)
  return biggest_number   





filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

legal_triplets = build_legal_triplets()

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  line = [int(v) for v in infile.readline().split()]
  
  N = line[0]
  S = line[1]
  p = line[2]
  t = line[3:]
  
  triplet_sets_for_scores = build_triplet_sets_for_scores(t, legal_triplets)
  print get_result(triplet_sets_for_scores, S, p)
  
  
  
infile.close()