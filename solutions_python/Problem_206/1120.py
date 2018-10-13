#s = "-+++-"    #state
#k = 4          #the num of pancakes

def calc(horses,D):
    road = {}
    for i in horses:
        k,s = i
        if k not in road:
            road[k]=s
        else:
            road[k]=min(road[k],s)
    maxTime = 0 
    for i in sorted(road.keys(), reverse=True):
        horseTime=(D-i+0.0)/road[i]
        if horseTime>maxTime:
            maxTime=horseTime
    return(D/maxTime)


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1): 
  D, N = [int(x) for x in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #print D
  #print N
  horses=[]
  for j in xrange(N):
    k, s = [int(x) for x in raw_input().split(" ")]  # read a list of integers, 2 in this case
    horses.append((k,s))
  res = calc(horses,D)
  print "Case #{}: {}".format(i, res)
  # check out .format's specification for more formatting options
  
  
  
#print flipPanckes(s,k)