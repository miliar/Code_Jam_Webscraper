import sys
data = sys.stdin.readlines()


i=1
while ( i < len(data)):
  line = data[i]
  inputs = line.split()
  low = int(inputs[0])
  high = int(inputs[1])
  pairs = 0
  x = low
  while x <= high:
    num_digits = len(str(x))
    q=1
    found = []
    while q < num_digits:
      strX = str(x)
      newStrX = strX[(q*-1):] + strX[0:len(strX)-q]
      if int(newStrX) >= low and int(newStrX) <= high and not ( int(newStrX) == int(strX)) and not((strX, newStrX) in found):
        found.append( (strX, newStrX))
       # print  strX + ":" + newStrX
        pairs = pairs + 1
      q = q+1 
    x= x+1
  
  print "Case #" + str(i) + ": " + str(pairs/2)
  i=i+1
  
  
