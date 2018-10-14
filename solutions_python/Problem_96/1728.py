import sys


infile = file("B-large.in",'r')
#infile = file("test.txt",'r')
count = 0
Sol = 0
Eligible = 0
LastString = ''
for line in infile :
        pp =''
        if count == 0:
                lcase = int(line.lstrip('\n'))
        else :
                info = line.split()
                print info
                N = int(info[0])
                S = int(info[1])
                P = int(info[2])
                Eligible = 0
                surp = 0
                for i in range (3, (N+3)) :
                  Nsurp = 0
                  CS = int(info[i])
                  B = int(CS/3)
                  BL = B-1
                  BP = B+1
                  BMin = B-2
                  BMax = B+2
                  Min = P-2
                  Max = P+2
                  if(((CS>0)or(B>0)or(BL>0)or(BMin>0))and(0<=P<=10)) :
                          if (B>P):
                              Eligible = Eligible + 1
                          elif((P==B)or(P==BL)or(P==BP)or(P==BMin)or(P==BMax)): # P is value that we care
                              if ((P+(P-1)+(P-1)==CS)or(P+(P+1)+(P+1)==CS)or((P*3)==CS)or(P+P+(P-1)==CS)or(P+P+(P+1)==CS)):
                                   Eligible = Eligible + 1
                              else :
                                   if(S>=1) :
                                        if(((P+(P-1)+(P+1))==CS)or((P+(P-2)+(P-2))==CS)or((P+(P+2)+(P+2))==CS)or((P+P+(P-2))==CS)or((P+P+(P+2))==CS)or((P+(P-1)+(P-2))==CS)or((P+(P+1)+(P+2))==CS)) :      
                                             S = S-1
                                             Eligible = Eligible + 1
                  elif (P==0) :
                          Eligible = Eligible + 1
                          print "P is ZERO"
                pp = 'Case #'+str(count)+': '+str(Eligible)
                if 0 < count < lcase :
                        LastString = LastString+pp+'\n'
                elif (count == lcase) :
                        LastString = LastString+pp
        count = count + 1
print LastString

fo = open("P2L.out", "w")
fo.write(LastString);
#close opend file
fo.close()

