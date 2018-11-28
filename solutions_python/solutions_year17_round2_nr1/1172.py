# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  #print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
  maxdist=n #D in problem
  maxtime=0
  for h in range(m):#no of horses
      k,s=[int(s) for s in input().split(" ")]
      #k=position, s= speed km/hr
      #calc maxtime to get to D
      thismaxtime=(maxdist-k)/s#in hours
      if thismaxtime>maxtime:
          maxtime=thismaxtime
  #we've found maxtime - so what speed
  maxspeed=maxdist/maxtime
  print("Case #{}: {}".format(i,maxspeed))# {}".format(i, n + m, n * m))
  
