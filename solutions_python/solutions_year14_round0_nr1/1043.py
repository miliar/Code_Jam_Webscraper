#!/usr/bin/python3
import fileinput
f=fileinput.input()
T=int(f.readline())
for case in range(T):
  a1=int(f.readline())-1
  grid1=[]
  for n in range(4):
    row=f.readline().strip().split()
    grid1.append(row)
  a2=int(f.readline())-1
  grid2=[]
  for n in range(4):
    row=f.readline().strip().split()
    grid2.append(row)
  guess=set(grid1[a1]).intersection(set(grid2[a2]))
  guessnum=len(guess)
  if guessnum==0:
    answer="Volunteer cheated!"
  elif guessnum==1:
    answer=guess.pop()
  else:
    answer="Bad magician!"
  print("Case #"+str(case+1)+":",answer)

      