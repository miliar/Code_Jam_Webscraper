import sys, math

iFile = open(sys.argv[1],"r")

size = int(iFile.readline().strip())

for case in range(size):

  diners = int(iFile.readline().strip())
  plates = [int(x) for x in iFile.readline().strip().split()]
  
  min_time = max(plates) 

  for height in range(1,max(plates)):
      cuts = 0
      for plate in plates:
          cuts += math.ceil(plate / height) - 1
      time = cuts + height
      min_time = min(min_time,time)

  output = str(min_time)
  
  print("Case #"+str(case+1)+": "+output)
