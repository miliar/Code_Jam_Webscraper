
import sys


def computeTime(pattern):
  O_pos = 1
  B_pos = 1
  t = 0

  O_dst = 1
  B_dst = 1

  O_lock = False
  B_lock = False

  O_dir_fwd = True
  B_dir_fwd = True

  while len(pattern):

    seq = pattern[0]

    if seq[0] == "O":
      O_lock = True
      B_lock = False
    else:
      O_lock = False
      B_lock = True
  

    for each in pattern:
      if 'O' in each:
        O_dst = each[1]
        if O_dst >= O_pos:
          O_dir_fwd = True
        else:
          O_dir_fwd = False
        break
      else:
        O_dst = O_pos

    for each in pattern:
      if 'B' in each:
        B_dst = each[1]
        if B_dst >= B_pos:
          B_dir_fwd = True
        else:
          B_dir_fwd = False
        break
      else:
        B_dst = B_pos


    t = t + 1
    #print "Time: ", t

    if O_pos == O_dst and O_lock == True:
      del pattern[0]
      #print "Orange Push ", O_pos
    elif O_dir_fwd == True and O_pos != O_dst:
      O_pos = O_pos+1
    elif O_dir_fwd == False and O_pos != O_dst:
      O_pos = O_pos-1

    if B_pos == B_dst and B_lock == True:
      del pattern[0]
      #print "Blue Push ", B_pos
    elif B_dir_fwd == True and B_pos != B_dst:
      B_pos = B_pos+1
    elif B_dir_fwd == False and B_pos != B_dst:
      B_pos = B_pos-1

    #print "O_dst: ", O_dst
    #print "B_dst: ", B_dst
    #print pattern
    #print "Orange ", O_pos
    #print "Blue ", B_pos
    #print ""

  return t


pattern1 = [('O',2),('B',1),('B',2),('O',4)]
pattern2 = [('O',5),('O',8),('B',100)]
pattern3 = [('B',2),('B',1)]


#print computeTime(pattern1)
#print computeTime(pattern2)
#print computeTime(pattern3)


inFile = open(sys.argv[1])

outFile = open("output.txt","w")

testcases = inFile.readline();


pattern = []
count = 1
for line in inFile:
  pattern = []
  testLine = line.split()
  buttons = int(testLine[0])
  #print "Line: ", testLine
  #print "Buttons: ", buttons
  i = 1
  while i < buttons*2:
   pattern.append((testLine[i],int(testLine[i+1])))
   i = i + 2
  #print "Pattern: ", pattern
  time = computeTime(pattern)

  resultStr = "Case #" + str(count) + ": " + str(time) + "\n"
  #print resultStr
  outFile.write(resultStr)
  count = count + 1

outFile.close()
inFile.close()
