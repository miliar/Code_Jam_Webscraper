import itertools

f = open('B-small.in','r')
fo = open('B-small.out','w')
cases = int(f.readline())

def maximum(trip, surp, targ):
  if (len(trip) == 0):
    return 0
  else:
    first = trip[0]
    possible = []
    for triplet in first:
      if (max(triplet) - min(triplet) == 2 and surp == 0):
        possible.append(0)
      else:
        if (max(triplet) - min(triplet) == 2):
          x = maximum(trip[1:], surp-1, targ)
        else:
          x = maximum(trip[1:], surp, targ)
        if (max(triplet) >= targ):
          possible.append(1 + x)
        else:
          possible.append(x)
    if (len(possible) == 0):
      return 0
    else:
      return max(possible)

for case in range(1, cases+1):
  line = f.readline()[:-1]
  items = line.split(' ')
  googlers = int(items[0])
  surprises = int(items[1])
  target = int(items[2])
  scores = items[3:]

  triplets = []
  for googler in range(0, googlers):
    triplets.append([])

    for a in range(0, 11):
      for b in range(a, min(11,a+3)):
        for c in range(a, min(11,a+3)):
          if (a + b + c == int(scores[googler])):
            triplets[googler].append((a, b, c))

  result = maximum(triplets, surprises, target)

  fo.write('Case #{}: {}\n'.format(case, result))

f.close()
fo.close()
