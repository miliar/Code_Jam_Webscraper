
T = input()
for i in range(1,T+1):
  row_i = input()
  for r in range(1,5):
    row = raw_input()
    if r==row_i:
      nums1 = map(int,row.split())
  row_i = input()
  for r in range(1,5):
    row = raw_input()
    if r==row_i:
      nums2 = map(int,row.split())
  result = set(nums1).intersection(set(nums2))
  l = len(result)
  if(l==1):
    print "Case #%d: %d" % (i,result.pop()) 
  elif(l==0):
    print "Case #%d: Volunteer cheated!" % i
  else:
    print "Case #%d: Bad magician!" % i
