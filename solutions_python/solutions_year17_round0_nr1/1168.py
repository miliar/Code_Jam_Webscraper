#s = "-+++-"    #state
#k = 4          #the num of pancakes

def flipPanckes(s,k):
    slist = list(s)
    cnt = 0
    
    for i in xrange(len(slist)-k+1):
        if slist[i]=="+":
            continue
        else:
            cnt+=1
            for j in xrange(k):
                if slist[i+j]=="+": 
                    slist[i+j]="-"
                else:
                    slist[i+j]="+"
    
    for i in xrange(len(slist)-1,k-2,-1):
        if slist[i]=="+":
            continue
        else:
            cnt+=1
            for j in xrange(k):
                if slist[i-j]=="+": 
                    slist[i-j]="-"
                else:
                    slist[i-j]="+"
        
    if "-" in slist:
        return "IMPOSSIBLE"
    else:
        return cnt




# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  s, k = [x for x in raw_input().split(" ")]  # read a list of integers, 2 in this case
  k = int(k)
  #print s
  #print k
  res = flipPanckes(s,k)
  print "Case #{}: {}".format(i, res)
  # check out .format's specification for more formatting options
  
  
  
#print flipPanckes(s,k)