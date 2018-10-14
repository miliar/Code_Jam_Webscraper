inputFile = open('A-large.in', 'r')

outputFile = open('output1-Large', 'w')


nbTests = int(inputFile.readline())

for i in range(nbTests):
  smax, repartition = inputFile.readline().split()
  smax = int(smax)
  
  result = 0
  nbDebouts = int(repartition[0])

  for j in range(1, smax+1):
    aRajouter = max(j - nbDebouts, 0)
    nbDebouts += aRajouter + int(repartition[j])
    result += aRajouter

  outputFile.write("Case #" + str(i + 1) + ": " + str(result) + "\n")
