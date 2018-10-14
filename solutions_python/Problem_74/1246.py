input = open('A-large (1).in', 'r')
output = open('A-large (1).out', 'w')

number = input.readline()
#print "number=>", number,"\n"

for line in range(int(number)):
 #print line
 seq = []
 O = []
 B = []
 index = 0
 Oindex = 0
 Bindex = 0
 time = 0

 Opos = 1
 Bpos = 1

 total = input.readline().split()

 for iter in range(len(total)):
  if total[iter] == "O":
   O = O + [total[iter+1]]
   seq = seq + ["O"]
  elif total[iter] == "B":
   B = B + [total[iter+1]]
   seq = seq + ["B"]

 #print "O = ", O
 #print "B = ", B
 #print "seq = ", seq

 while index < len(seq):
  #print "index =", index, "len(seq)=", len(seq)
  if seq[index] == "O":
   if Opos < int(O[Oindex]):
    Opos = Opos + 1
    time = time + 1
   elif Opos > int(O[Oindex]):
    Opos = Opos - 1
    time = time + 1
   elif Opos == int(O[Oindex]):
    index = index + 1
    Oindex = Oindex + 1
    time = time + 1

   if Bindex < len(B):
    if Bpos < int(B[Bindex]):
     Bpos = Bpos + 1
    elif Bpos > int(B[Bindex]):
     Bpos = Bpos - 1


  if index < len(seq) and seq[index] == "B":
   if Bpos < int(B[Bindex]):
    Bpos = Bpos + 1
    time = time + 1
   elif Bpos > int(B[Bindex]):
    Bpos = Bpos - 1
    time = time + 1
   elif Bpos == int(B[Bindex]):
    index = index + 1
    Bindex = Bindex + 1
    time = time + 1

   if Oindex < len(O):
    if Opos < int(O[Oindex]):
     Opos = Opos + 1
    elif Opos > int(O[Oindex]):
     Opos = Opos - 1
  #print "Time=",time,"Opos=",Opos,"Bpos=",Bpos
 #print "--------------------"
 output.write('Case #' + str(line+1) + ': ' + str(time) + "\n")