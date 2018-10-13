import math
T = input()
for i in range(1,T+1):
  R,C,M = map(int,raw_input().split())
  print "Case #%d:" % i
  empties = R*C-M
  if R==1:
    print "*"*M+"."*(empties-1)+"c"
  elif C==1:
    print "*\n"*M+".\n"*(empties-1)+"c"
  elif empties==1:
    for i in range(R-1):
      print "*"*C
    print "*"*(C-1)+"c"
  elif R==2:
    if empties%2==1 or empties==2:
      print "Impossible"
    else:
      print "*"*(M/2)+"."*(C-M/2)
      print "*"*(M/2)+"."*(C-M/2-1)+"c"
  elif C==2:
    if empties%2==1 or empties==2:
      print "Impossible"
    else:
      for i in range(M/2):
        print "**"
      for i in range(R-1-M/2):
        print ".."
      print ".c"
  elif empties>=8:
    if M<=(R-3)*C:
      if C-M%C != 1:
        for i in range(M/C):
          print "*"*C
        print "*"*(M%C)+"."*(C-M%C)
        for i in range((empties-1)/C-1):
          print "."*C
        print "."*(C-1)+"c"
      else:
        for i in range(M/C):
          print "*"*C
        print "*"*(M%C-1)+"."*(C-M%C+1)
        print "*"+"."*(C-1)
        for i in range((empties-1)/C-2):
          print "."*C
        print "."*(C-1)+"c"
    else:
      for i in range(R-3):
        print "*"*C
      rest = M-(R-3)*C
      a = rest/3 + rest%3
      b = rest/3
      print "*"*a+"."*(C-a)
      print "*"*b+"."*(C-b)
      print "*"*b+"."*(C-b-1)+"c"
  elif empties==6:
    for i in range(R-2):
      print "*"*C
    print "*"*(C-3)+"..."
    print "*"*(C-3)+"..c"
  elif empties==4:
    for i in range(R-2):
      print "*"*C
    print "*"*(C-2)+".."
    print "*"*(C-2)+".c"
  else:
    print "Impossible"
