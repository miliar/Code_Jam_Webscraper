import sys, math

filename = sys.argv[1]

data = open(filename, 'r')
output = open('output2.dat', 'w')

n_cases = int(data.readline())
f = lambda x,y: math.ceil((x-y)/2.0)
g = lambda x,y,z: x-y-z
for i in range(n_cases):
  line = data.readline().rstrip()
  splitted = line.split()
  googlers = int(splitted[0])
  surprising = int(splitted[1])
  top_score = int(splitted[2])
  results = splitted[3:]
  results = map(float, results)
  first_results = [math.ceil(x/3.0) for x in results]
  second_results = [f(x,y) for x,y in zip(results, first_results)]
  third_results = [g(x,y,z) for x,y,z in zip(results, first_results, second_results)]
  score_tuple = []
  max_scores = []
  score = 0
  for j in range(googlers):
    score_tuple.append((first_results[j],second_results[j],third_results[j]))
    max_scores.append(max(score_tuple[j]))
    a = max_scores[j]-min(score_tuple[j])
    if a> 1:
      print 'incorrect'
    if max_scores[j] >= top_score:
      score += 1
    elif surprising != 0:
      #print 'surprise'
      maximum = max_scores[j] + 1
      minimum = min(score_tuple[j]) - 1
      if  maximum <= 10 and maximum >= top_score and minimum >= 0:
	surprising -= 1
	a = (max_scores[j]+1)-(min(score_tuple[j])-1)
	if a > 2:
	  minimum += 1
	  counter = 0
	  for k in score_tuple[j]:
	    if minimum == k:
	      counter += 1
	  if not (counter > 1):
	    score += 1
	    #print score_tuple[j], top_score, results[j], i
	else:
	  score += 1
  output.writelines('Case #'+str(i+1)+': '+str(score)+'\n')