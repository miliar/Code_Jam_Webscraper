def findBiggestTidy(N):
    Nlist = list(str(N))
    #print Nlist
    for i in xrange(1,len(Nlist)):
        if Nlist[-i]<Nlist[-i-1]:
            for j in xrange(1,i+1):
                Nlist[-j]='9'
            Nlist[-i-1]=str(int(Nlist[-i-1])-1)
            #print Nlist    
    return int("".join(Nlist))
    

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  N, = [int(x) for x in raw_input().split(" ")]  # read a list of integers, 2 in this case
  #print N
  res = findBiggestTidy(N)
  print "Case #{}: {}".format(i, res)
  # check out .format's specification for more formatting options

  
  
