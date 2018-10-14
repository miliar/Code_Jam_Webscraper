f = open("A-small-attempt0.in","r")
floc = int(f.readline())
out = open("derp.out","wa")



for ca in range(floc):
  line1 = int(f.readline())-1
  list1 = [f.readline().replace("\n","").split(" ") for i in range(4)]
  line2 = int(f.readline())-1
  list2 = [f.readline().replace("\n","").split(" ") for i in range(4)]
  choice1 = set(list1[line1])
  choice2 = set(list2[line2])
  result = choice1 & choice2
  if len(result) == 1:
    out.write("Case #%d: %s\n" % (ca+1, list(result)[0])) 
  elif len(result) == 0:
    out.write("Case #%d: Volunteer cheated!\n" % (ca+1))
  else:
    out.write("Case #%d: Bad magician!\n" % (ca+1))



out.close()

