
f = open("tiles1.in")
f2 = open("tiles1.out", "w")

lines = f.readlines()


cur = 1
testcases = int(lines[0])
for testcase in range(testcases):
  params = lines[cur].split()
  height = int(params[0])
  width = int(params[1])
  
  wall_tmp = map(lambda a: a.strip(), lines[cur + 1:cur + 1 + height])

  wall = [[' ' for i in range(width)] for j in range(height)]
  for ii in range(height):
    for jj in range(width): 
      wall[ii][jj] = wall_tmp[ii][jj]

  def ok(row, col):
   if row < 0 or row >= height:
     return False
   if col < 0 or col >= width:
     return False
   return wall[row][col] == '#'
   
  missed = False
  for row in range(height):
   for col in range(width):
     if ok(row, col):
       sq1 = ok(row, col)
       sq2 = ok(row, col + 1)
       sq3 = ok(row + 1, col)
       sq4 = ok(row + 1, col + 1)
       overall = sq1 and sq2 and sq3 and sq4
       if overall:
         wall[row][col] = '/'
         wall[row][col + 1] = '\\'
         wall[row + 1][col] = '\\'
         wall[row + 1][col + 1] = '/'
       else:
         missed = True
         break
         break        
  f2.write("Case #%d:\n" % (testcase + 1))
  if missed:
    f2.write("Imposibble\n")
  else:
    for i in range(height):  
      ss = "".join(str(wall[i][zz]) for zz in range(width))
      f2.write(ss + "\n")
  cur += height + 1
  

f.close()
f2.close()
