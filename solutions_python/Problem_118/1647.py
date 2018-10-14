import math

precomp = [1, 121, 4, 484, 9, 10201, 1002001, 12321, 1234321, 14641, 40804, 4008004, 44944, 100020001, 10000200001, 102030201, 10221412201, 104060401, 121242121, 12102420121, 123454321, 12345654321, 125686521, 400080004, 40000800004, 404090404, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004] 
for c in xrange(int(raw_input())):
  a, b = map(int, raw_input().split())
  print "Case #"+str(c+1)+":", len(filter(lambda x: a <= x <= b, precomp))
  
busy_precomputing = False
if busy_precomputing:
  a_r = int(math.sqrt(a))
  b_r = int(math.sqrt(b) + 1)
  # Same number of digits
  # Get prefix, count all with prefix

  # Different powers
  # Generate all with all powers in between
  #odd = len(str(a))%2 == 1
  start = 10**(len(str(a_r-1))-1)
  end = 10**(len(str(b_r)))

  count = 0
  pals = []
  for i in xrange(start, end+1):
    #Odd
    odd = int(str(i)+str(i)[-2::-1])
    if a_r <= odd <= b_r:
      squared = odd**2
      if a <= squared <= b:
        if str(squared) == str(squared)[::-1]:
          count+=1
          pals.append(squared)

    #Even
    even = int(str(i)+str(i)[::-1])
    if a_r <= even <= b_r:
      squared = even**2
      if a <= squared <= b:
        if str(squared) == str(squared)[::-1]:
          count+=1
          pals.append(squared)
  print count 
  print pals

