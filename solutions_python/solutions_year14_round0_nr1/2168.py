f1 = open('C:\Personal\QuickCommands\A-small-attempt1.in', 'r')
f2 = open('C:\Personal\QuickCommands\magic_output.txt', 'w')

linenum = 0;
possibilities = [];
casenum = 0;
answer = -1;
checkAnswer = False;

for line in f1:
   if linenum > 0:
      if (linenum -1) % 5 == 0:
         answer = int(line) + linenum;
         if (linenum -1) % 2 != 0: #this is the second pass
            casenum += 1;
            casestr = 'Case #' + str(casenum) + ': ';
            checkAnswer = True;
      
      elif checkAnswer and linenum == answer:
         count = 0;
         final = [int(x.strip()) for x in line.split(' ')];
         solution = -1
         
         for card in final:
            if card in possibilities:
               solution = card;
               count += 1;
         
         retval = '';
         if count == 0:
            retval = 'Volunteer cheated!';
         elif count == 1:
            retval = solution;
         else:
            retval = 'Bad magician!';
         
         #print(casestr, str(retval));
         retval = casestr + str(retval) + '\n';
         f2.write(retval);
         checkAnswer = False;
      
      elif linenum == answer:
         possibilities = [int(x.strip()) for x in line.split(' ')];
   linenum += 1;
f1.close();
f2.close();