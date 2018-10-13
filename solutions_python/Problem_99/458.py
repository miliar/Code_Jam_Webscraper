#!/usr/bin/env python

#fin = open("sampleinput.txt")
#fout = open("sampleoutput.txt", "w")

fin = open("A-small-attempt0.in.txt")
fout = open("A-small-attempt0.out.txt", "w")

#fin = open("A-large.in.txt")
#fout = open("A-large.out.txt", "w")

T = int(fin.readline().strip())
for X in range(1,T+1):
  A, B = map(int, fin.readline().strip().split(" "))
  probabilities = map(float, fin.readline().strip().split(" "))
  print "A,B: " + str(A) + "," + str(B)

  # "numBack = -1": Press enter right away
  expect = B + 2

  for numBack in range(0,A+1):
    print numBack
    if (A-numBack>0):
      probRight = reduce(lambda x, y: x * y, probabilities[0:A-numBack])
    else:
      probRight = 1
    keyIfRight = B - A + 1 + 2*numBack
    keyIfWrong = (B - A + 1 + 2*numBack) + (B + 1)
    tempExpect = probRight * keyIfRight + (1 - probRight) * keyIfWrong

    print "keyIfRight, probRight, keyIfWrong: " + str(keyIfRight) + ", " + str(probRight) + ", " + str(keyIfWrong)
    print "tempExpect: " + str(tempExpect)
    if (tempExpect<expect):
      expect = tempExpect

  fout.write("Case #" + str(X) + ": " + str(expect) + "\n")

fin.close()
fout.close()
