# Recycled Numbers

# main code

fr = open('C-large.in', 'r')
fw = open('C-large.out', 'w')

numOfTestCase = int(fr.readline())

for x in range(0,numOfTestCase):
  result = ""
  print("========== Test case " + str(x+1) + " ==========")

  line = fr.readline()
  line = line.split(" ")
  A = int(line[0])
  B = int(line[1])

  # initialize number of distinct recycle number
  nDistinct = 0

  for i in range(A,B+1):
    # change to string
    i_str = str(i)
    i_str_recycle = i_str
    strlen = len(i_str)

    if strlen == 1:
      # No recycle number possible
      continue

    from array import array
    pairList = array('i')
    
    for j in range(0,strlen):
      i_str_recycle = i_str_recycle[strlen-1] + i_str_recycle[0:strlen-1]

      if i_str_recycle != i_str and i_str_recycle[0] != '0' and (A <= int(i_str_recycle) and int(i_str_recycle) <= B) and int(i_str_recycle) > i :
        # i_str_recycle should not be the same as i_str
        # i_str_recycle should not be lead with digit 0
        # i_str_recycle should not be in range A to B inclusive
        # i_str_recycle should be bigger than i

        repeatFlag = 0

        # finally, there should be no repeat pair
        for k in range(0,len(pairList)):
          if pairList[k] == int(i_str_recycle):
            repeatFlag = 1

        if repeatFlag == 0:
          nDistinct = nDistinct + 1
          # print(i_str + ", " + i_str_recycle)
          # put current pair to pairList to prevent double pair
          pairList.append(int(i_str_recycle))
      
  result = str(nDistinct)

  fw.write("Case #" + str(x+1) + ": " + result + "\n")

fr.close()
fw.close()
