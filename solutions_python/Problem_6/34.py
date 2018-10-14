I created a Mathematica function F[n_] := N[Floor[Mod[(3 + Sqrt[5])^n, 1000]]], then used python to output a string I could copy into mathematica as a list, used Mathematica's Map function to map F to each of the input integers, and used another python function to output the solution:

Input: 
f = open(filename)
numCases = int(f.readline())
print "{",
for case in range(1, numCases + 1):
  num = int(f.readline().strip())
  print num,
  if (case != numCases):
  print ",",
print "}"

Output:
l = map(lambda x:int(x[:-1]), "{5., 27., 143., 751.}"[1:-1].split(','))
for x in range(1, len(l)+1): print 'Case #'+str(x)+': %(#)03d' % {"#" : l[x-1]}