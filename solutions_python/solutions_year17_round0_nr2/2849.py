 
 # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):
  n = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

  n=n[0]
  val=int(n)

  flag=0
  while(flag==0):
    # print val
    flag=1
    NewN=list(n)
    size= len(NewN)
    if size==1:
      flag=1
      val=val-1
      break
    for j in range(0,size-1):
      # print "compare #{}: {}".format(NewN[j], NewN[j+1])
      if(int(NewN[j])>int(NewN[j+1])):
        flag=0
      # else:
      #   flag=1
    val=val-1
    n=str(val)
    val=int(n)


  print "Case #{}: {}".format(i, val+1 )
  

 