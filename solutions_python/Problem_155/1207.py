import string

inputFile = open('ovation-large.in', 'r')
inputData = inputFile.read().strip()

numCases  = int(inputData.split('\n')[0])
cases     = inputData.split('\n')


def computeShyCount(index, shyCounts):

  friendsNeeded  = 0
  peopleStanding = 0
  for rating in xrange(len(shyCounts)):
    if rating > peopleStanding + friendsNeeded:
      friendsNeeded += rating - peopleStanding - friendsNeeded
    peopleStanding += shyCounts[rating]

  return "Case #" + str(i) + ": " + str(friendsNeeded)


for i in xrange(1, numCases+1):
  case = cases[i]
  shyness, shyCounts = case.split(' ')
  shyCounts = [int(x) for x in shyCounts]

  print computeShyCount(i, shyCounts)


