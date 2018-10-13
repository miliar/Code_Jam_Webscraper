f = open('A-large.in', 'r')
g = open('output', 'w')

test_cases = int(f.readline())

for i in range(1, test_cases+1):
   result = ""
   draw_impossible = False
   test_case = []
   for j in range(4):
      test_case.append(f.readline())
   for j in range(4):
      X = 0
      O = 0
      for k in range(4):
         if test_case[j][k] == '.':
            draw_impossible = True
         elif test_case[j][k] == 'X':
            X += 1
         elif test_case[j][k] == 'O':
            O += 1
         elif test_case[j][k] == 'T':
            X += 1
            O += 1
      if X == 4:
         result = "X won"
      elif O == 4:
         result = "O won"
   if result == "":
      for j in range(4):
         X = 0
         O = 0
         for k in range(4):
            if test_case[k][j] == '.':
               draw_impossible = True
            elif test_case[k][j] == 'X':
               X += 1
            elif test_case[k][j] == 'O':
               O += 1
            elif test_case[k][j] == 'T':
               X += 1
               O += 1
         if X == 4:
            result = "X won"
         elif O == 4:
            result = "O won"
   if result == "":
      X = 0
      O = 0
      for j in range(4):
         if test_case[j][j] == 'X':
            X += 1
         elif test_case[j][j] == 'O':
            O += 1
         elif test_case[j][j] == 'T':
            X += 1
            O += 1
      if X == 4:
         result = "X won"
      elif O == 4:
         result = "O won"
   if result == "":
      X = 0
      O = 0
      for j in range(4):
         if test_case[3-j][j] == 'X':
            X += 1
         elif test_case[3-j][j] == 'O':
            O += 1
         elif test_case[3-j][j] == 'T':
            X += 1
            O += 1
      if X == 4:
         result = "X won"
      elif O == 4:
         result = "O won"
   if result == "":
      if not(draw_impossible):
         result = "Draw"
      else:
         result = "Game has not completed"
   print "Case #" + str(i) + ": " + result
   g.write("Case #" + str(i) + ": " + result + "\n")
   f.readline()
