def minimumExchanges(cameron, jamie):
  events = [(C, D, 'c') for (C, D) in cameron] + [(J, K, 'j') for (J, K) in jamie]
  sortedEvents = sorted(events)
  otherPerson  = {}
  otherPerson['c'] = 'j'
  otherPerson['j'] = 'c'
  result = 10000
  for startingPerson in 'cj':
    # states are indexed by minutes for cameron so far and the current owner, and return fewest exchanges
    optimalStates = {}
    optimalStates[(0, startingPerson)] = 0
    currentEventIndex = 0
    currentEventStart = sortedEvents[currentEventIndex][0]
    currentEventEnd   = sortedEvents[currentEventIndex][1]
    currentEventOwner = sortedEvents[currentEventIndex][2]
    for i in xrange(1440):
      newOptimalStates = {}
      for (Cminutes, owner) in optimalStates:
        # Exchange if possible
        if i < currentEventStart or i >= currentEventEnd or currentEventOwner != otherPerson[owner]:
          newState = (Cminutes + (1 if otherPerson[owner] == 'c' else 0), otherPerson[owner])
          newOptimalStates[newState] = min(newOptimalStates.get(newState, 10000), optimalStates[(Cminutes, owner)] + 1)
        # Hold if possible
        if i < currentEventStart or i >= currentEventEnd or currentEventOwner != owner:
          newState = (Cminutes + (1 if owner == 'c' else 0), owner)
          newOptimalStates[newState] = min(newOptimalStates.get(newState, 10000), optimalStates[(Cminutes, owner)])
      if i + 1 == currentEventEnd:
        if currentEventIndex + 1 < len(events):
          currentEventIndex += 1
          currentEventStart  = sortedEvents[currentEventIndex][0]
          currentEventEnd    = sortedEvents[currentEventIndex][1]
          currentEventOwner  = sortedEvents[currentEventIndex][2]
        else:
          currentEventIndex = -1
          currentEventStart = -1
          currentEventEnd   = -1
          currentEventOwner = None
      optimalStates = newOptimalStates
    result = min(result, optimalStates.get((720, startingPerson), 10000))
    result = min(result, optimalStates.get((720, otherPerson[startingPerson]), 10000) + 1)
  return result

with open('../inputs/B-large.in') as infile:
  with open('../outputs/B-large.out', 'wb') as outfile:
    cases = int(infile.readline())
    for i in xrange(cases):
      [Ac, Aj] = map(int, infile.readline().split(' '))
      cameron  = []
      jamie    = []
      for _ in xrange(Ac):
        [C, D] = map(int, infile.readline().split(' '))
        cameron.append((C, D))
      for _ in xrange(Aj):
        [J, K] = map(int, infile.readline().split(' '))
        jamie.append((J, K))
      outfile.write('Case #' + str(i + 1) + ': ')
      outfile.write(str(minimumExchanges(cameron, jamie)))
      outfile.write('\n')
