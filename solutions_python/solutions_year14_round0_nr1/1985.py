f=open("A-small-attempt0.in","r")
out = open('workfile', 'w')
T=int(f.readline())

for x in range(T):

  answer1=int(f.readline())

  rows=[str(f.readline()).split(),str(f.readline()).split(),\
        str(f.readline()).split(),str(f.readline()).split()]

  options=rows[answer1-1]

  answer2=int(f.readline())

  secondrows=[str(f.readline()).split(),str(f.readline()).split(),\
              str(f.readline()).split(),str(f.readline()).split()]

  picked_card=[]
 
  for card in secondrows[answer2-1]:
    if card in options:
      picked_card.append(card)

  if len(picked_card)==0:
    out.write("Case #"+str(x+1)+": Volunteer cheated!\n")
  elif len(picked_card)==1:
    out.write("Case #"+str(x+1)+": "+str(picked_card[0])+"\n")
  elif len(picked_card)>1:
    out.write("Case #"+str(x+1)+": Bad magician!\n")

