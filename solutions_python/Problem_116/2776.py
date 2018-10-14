#!/usr/bin/python3

def diasearch(dia):

   if (dia[0] == '.'):
      return 0

   if ('T' in dia):
      if (dia.count(dia[0]) + dia.count('T') == 4):
         return dia[0]
   else:
      if (dia.count(dia[0]) == 4):
         return dia[0]

   return 0
#end diacount

#return winner
def search(ttt):
   for i in range(4):

      if (ttt[i][0] == '.'):
         continue

      if ('T' in ttt[i]):
         if (ttt[i].count(ttt[i][0]) + ttt[i].count('T') == 4):
            return ttt[i][0]
      else:
         if (ttt[i].count(ttt[i][0]) == 4):
            return ttt[i][0]

   return 0
#end search

def main():
   
   finput = open("A-small-attempt0.in", "r")
   foutput = open("testout.txt", "w+")

   while True:
   
      testtimes = finput.readline().split()
      if testtimes == []:
         break

      testtimes = int(testtimes[0])

      for i in range(testtimes):

         if (i >= 1):
            #eat empty line
            eatemptyline = finput.readline()

         ttt_row = []
         ttt_col = ["", "", "", ""]
         ttt_diagonal = ["", ""]
         
         for j in range(4):
            ttt_row.append(finput.readline().strip())
         for j in range(4):
            for k in range(4):
               ttt_col[j] += ttt_row[k][j]

         #search row by row
         tmp = search(ttt_row)
         if (tmp != 0):
            print("Case #"+str(i+1)+": "+tmp+" won")
            foutput.write("Case #"+str(i+1)+": "+tmp+" won\n")
            continue;


         #search column by column
         tmp = search(ttt_col)
         if (tmp != 0):
            print("Case #"+str(i+1)+": "+tmp+" won")
            foutput.write("Case #"+str(i+1)+": "+tmp+" won\n")
            continue;

         #search diagonal
         Ldia = ""
         Rdia = ""
         k = 0
         for j in range(4):
            Ldia += ttt_row[k][j]
            Rdia += ttt_row[k][3-j]
            k += 1

         tmp = diasearch(Ldia)
         if (tmp != 0):
            print("Case #"+str(i+1)+": "+tmp+" won")
            foutput.write("Case #"+str(i+1)+": "+tmp+" won\n")
            continue

         tmp = diasearch(Rdia)
         if (tmp != 0):
            print("Case #"+str(i+1)+": "+tmp+" won")
            foutput.write("Case #"+str(i+1)+": "+tmp+" won\n")
            continue

         #if the ttt full: print Draw
         #else: print Game has not completed
         dotcount = 0
         for j in range(4):
            for k in range(4):
               if (ttt_row[j][k] == '.'):
                  dotcount += 1
         
         if (dotcount != 0):
            print("Case #"+str(i+1)+": Game has not completed")
            foutput.write("Case #"+str(i+1)+": Game has not completed\n")
         else:
            print("Case #"+str(i+1)+": Draw")
            foutput.write("Case #"+str(i+1)+": Draw\n")
         
         
      #end for
   #end while   
   finput.close()
   foutput.close()

#end main()
main()
