fin = open('A-small-attempt3.in', 'r')
fout = open('output.txt','w')
T = eval(fin.readline())
t = 1
while t in range(1, T + 1) :
      ans1 = int(fin.readline())
      row = 0
      row1 = list()
      i = 1
      while i in range(1,4 + 1) :
            if i == ans1 :
                  row = list(fin.readline().split(' '))
            else :
                  fin.readline()
            i = i + 1
      i = 0
      while i in range(0,4) :
            row1.append( int(row[i]))
            i = i + 1
      ans2 =  int(fin.readline())
      row2 = list()
      i=1
      while i in range(1, 4 + 1) :
            if i == ans2 :
                  row = list(fin.readline().split(' '))
            else :
                  fin.readline()
            i = i + 1
      i = 0
      while i in range(0,4) :
            row2.append(int(row[i]))
            i = i + 1
      i = 0
      y = 0
      while i in range(0, 4) :
            j = 0
            while j in range(0,4) :
                  if row1[i] == row2[j] :
                        #print(i,j)
                        if y == 0:
                              y = row1[i]
                        else :
                              y = -1
                  j = j + 1
            i = i + 1
      #print(row1, row2)
      if y == 0:
            fout.write("Case #"+str(t) + ": Volunteer cheated!\n")
      elif y == -1 :
            fout.write("Case #"+str(t) + ": Bad magician!\n")
      else :
            fout.write("Case #"+str(t) + ": " + str(y) + "\n")
      t = t + 1     
fin.close()
fout.close()
