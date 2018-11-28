# keep an array of size N+2
# set the first and lastm index to True (occupied)


# for a given world state, and a person
#   calculate Ls and Rs:
#   set minWeight to 0
#   set S to []
#   for each index I:
#     check if its occupied
#     if not, iterate backwards until an occupied index I_lo is found
#     when found, subtract I_o from I -> Ls
#     now iterate forwards until an occupied index I_ro is found
#     when found, subtract I from I_ro -> Rs
#     the weighting for index I is min(I_lo, I_ro)
#     if the weighting is greater than the min weighting
#       S = [[I, Ls, Rs]]
#       minWeighting = weighting
#     if weighting is equal to minWeighting
#       S.append([I, Ls, Rs])
#     if weighing is less than minWeighting
#       continue
#   farthestNeigh = 0
#   refinedS = []
#   for s in S:
#     if max(s.Ls, s.Rs) > farthestNeigh:
#       farthestNeight = max(s.Ls, s.Rs)
#       refinedS = [I]
#     if max(s.Ls, s.Rs) == farthestNeight:
#       refinedS.append(I)
#   finalS = refinedS[0]

#   worldState[finalS] = True

#   if person is last person, return finalS


import sys
import fileinput

numTestCases = None
testCase = 0

for line in fileinput.input():
  if fileinput.isfirstline():
    numTestCases = int(line.rstrip())
    continue
  testCase += 1
  [N, K] = line.rstrip().split(' ')

  N = int(N)
  K = int(K)

  stalls = [False for i in range(N+2)]
  stalls[0] = True
  stalls[-1] = True

  lastPerson = None

  #For each person
  for k in range(K):
    minWeight = 0
    S = []
    leftOccupiedStallIndex = 0
    for sIndex in range(len(stalls)):
      stall = stalls[sIndex]
      #if stall is occupied, iterate to next
      if stall:
        #save this occupied value for use later
        leftOccupiedStallIndex = sIndex
        continue
      #calculate Ls and Rs
      Ls = sIndex - leftOccupiedStallIndex -1
      Rs = None
      #iterate forward to find the right occupied index
      for sIndexPrime in range(sIndex+1, len(stalls)):
        sPrime = stalls[sIndexPrime]
        if sPrime:
          Rs = (sIndexPrime - sIndex) - 1
          break
      weighting = min(Ls, Rs)
      s = {'index': sIndex, 'Ls': Ls, 'Rs': Rs}
      if weighting > minWeight:
        S = [s]
        minWeight = weighting
      elif weighting == minWeight:
        S.append(s)
    farthestNeigh = 0
    refinedS = []
    for s in S:
      if max(s['Ls'], s['Rs']) > farthestNeigh:
        farthestNeigh = max(s['Ls'], s['Rs'])
        refinedS = [s]
      elif max(s['Ls'], s['Rs']) == farthestNeigh:
        refinedS.append(s)
    finalS = refinedS[0]
    stalls[finalS['index']] = True
    lastPerson = finalS

  print "Case #"+str(testCase)+": "+str(max(lastPerson['Ls'], lastPerson['Rs']))+' '+str(min(lastPerson['Ls'], lastPerson['Rs']))




