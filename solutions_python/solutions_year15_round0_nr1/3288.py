

def shynessInd(size, shyness):
  while shyness[size] == '0':
    size -= 1
    if size == -1:
      return 0
 
  shyness = shyness[:size]
 
  current = 0
  need = 0
  for j in range(len(shyness)):
    current += int(shyness[j])
    if current <= j:
      current += 1
      need += 1
 
  return need





def main():

  myfile = open("A-large.in", 'r')
  output = open("outputlarge.txt", 'w')

  allFile = myfile.read()

  fileList = allFile.splitlines()
  numIN = int(fileList[0])
  del fileList[0]
  for x in range(0, numIN):
		sublist = fileList[x].split(" ")
		output.write("Case #" + str(x+1) + ": " +  str(shynessInd(int(sublist[0]), sublist[1])) + "\n")        
main()
