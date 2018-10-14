import math

def getFullSteps(num_of_people):
  num_of_people = num_of_people + 1
  return int(math.log(num_of_people, 2))

def getFreeSpaceLength(num_of_stalls, full_steps):
  powerOfSteps = pow(2, full_steps)
  placements = powerOfSteps - 1
  short = int((num_of_stalls - placements) / powerOfSteps)
  shortOccupied = short * powerOfSteps
  remaining = num_of_stalls - placements
  if remaining == shortOccupied:
    return [short, short, 0]
  else:
    return [short, short + 1, remaining - shortOccupied]


def solve(num_of_stalls, num_of_people):
  fullSteps = getFullSteps(num_of_people)
  intermediate = getFreeSpaceLength(num_of_stalls, fullSteps)
  lengthToPutLast = 0
  if num_of_people == pow(2, fullSteps) - 1:
    intermed2 = getFreeSpaceLength(num_of_stalls, fullSteps - 1)
    lengthToPutLast = intermed2[0]
  elif intermediate[0] == intermediate[1]:
    lengthToPutLast = intermediate[0]
  else:
    placesForGreater = intermediate[2]
    placementsForFullStep = pow(2, fullSteps) - 1
    remainingPlacements = num_of_people - placementsForFullStep
    if remainingPlacements > placesForGreater:
      lengthToPutLast = intermediate[0]
    else:
      lengthToPutLast = intermediate[1]
  if (lengthToPutLast % 2 != 0):
    return [int(lengthToPutLast / 2), int(lengthToPutLast / 2)]
  else:
    return [int(lengthToPutLast / 2), int(lengthToPutLast / 2) - 1]

def getResult(caseNum, num_of_stalls, num_of_people):
  result = solve(num_of_stalls, num_of_people)
  print("Case #" + str(caseNum)+": " + str(result[0]) + " " + str(result[1]))

numCases = int(input())
for i in range(numCases):
  caseNum = i + 1
  inputList = input().split()
  numStalls = int(inputList[0])
  numPeople = int(inputList[1])
  getResult(caseNum, numStalls, numPeople)
  
