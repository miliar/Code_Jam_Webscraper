import sys

targetDistance = 0
numberHorses = 0
maxEta = 0

def calculateSpeed():
  speed = targetDistance / maxEta
  print(targetDistance)
  print(maxEta)
  time = targetDistance / speed
  if(time < maxEta):
    print("Time/ETA discrepancy detected")
  return speed

def updateMax(data, counter):
  print("Updating max...")
  global maxEta
  asSplit = data.split(" ")
  start = int(asSplit[0])
  total = targetDistance - start
  speed = int(asSplit[1])
  print(str(total) + " " + str(speed))
  time = total / speed
  # if ETA is new max, update
  if(counter == 1 or time > maxEta):
    print("New val: "+str(time))
    maxEta = time

def processLineData(data):
  global numberHorses, targetDistance
  # split first and second numbers
  asSplit = data.split(" ")
  # get first number
  first = int(asSplit[0])
  targetDistance = first
  # get second number
  second = int(asSplit[1])
  numberHorses = second
  return second

def filer():
  global targetDistance, maxEta, numberHorses
  filepath = sys.argv[1]
  with open(filepath) as f:
    content = f.readlines()

  content = [x.strip() for x in content]
  newcontent = []

  casecounter = 1
  j = 1
  while (j<(len(content))):
    print("Case ####################")
    targetDistance = 0
    maxEta = 0
    numberHorses = 0
    data = processLineData(content[j])
    # process each horse line to find
    # minimum
    for i in range(data):
      updateMax(content[j+i+1], j)

    # calculate Annie speed
    speed = calculateSpeed()

    # skip processed lines
    j += (data+1)
    newcontent.append("Case #" + str(casecounter) + ": " + str("%.6f" % speed) + "\n")
    casecounter += 1

  target = open("output_numbers.txt", 'w')
  for i in range(len(newcontent)):
    line = content[i]
    target.write(newcontent[i])

def main():
  print("Running horses...")
  filer()

main()
