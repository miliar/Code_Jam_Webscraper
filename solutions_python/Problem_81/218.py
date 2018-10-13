def a_vs_b(a,b,matrix):
   return matrix[b][a]

def wp(team, matrix, exc):
   wins = 0.0
   loss = 0.0
   for i in xrange(len(matrix)):
      if i != exc and i != team:
         if matrix[team][i] == 'w':
            wins += 1.0
         elif matrix[team][i] == 'l':
            loss += 1.0
   wp = wins/(wins + loss)
   #print "wp: ",team,wp,wins,loss
   return wp

def owp(team, matrix):
   cowp = 0.0
   n = 0.0
   for i in xrange(len(matrix)):
      if i != team and matrix[team][i] != 'p':
         cowp += wp(i, matrix, team)
         n += 1.0
   owp = cowp/n
   #print "owp: ",team,owp
   return owp

def oowp(team, matrix):
   coowp = 0.0
   n = 0.0
   for i in xrange(len(matrix)):
      if i != team and matrix[team][i] != 'p':
         coowp += owp(i, matrix)
         n += 1.0
   oowp = coowp/n
   return oowp

def rpi(team, matrix):
   rpi = 0.25*wp(team, matrix, -1) + 0.50*owp(team, matrix) + 0.25*oowp(team, matrix)
   return rpi

test_cases = int(raw_input())

for i in xrange(test_cases):
   num_teams = int(raw_input())
   score_matrix = []
   for j in xrange(num_teams):
      nl = raw_input()
      nr = []
      for c in nl:
         if c == '1':
            nr.append('w')
         elif c == '0':
            nr.append('l')
         elif c == '.':
            nr.append('p')
      score_matrix.append(nr)
   print "Case #" + str(i + 1) + ":"
   for j in xrange(num_teams):
      print str(rpi(j, score_matrix))
