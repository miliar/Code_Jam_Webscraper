f = open('A-small-attempt0.in', 'r+')


numberOfCase = int(f.readline())

for case in range(1, numberOfCase + 1):
  cardsVolunteer = set()
  rowVolunteer1 = int(f.readline())
  for i in range(4):
    rowCards = f.readline().split()
    if i == rowVolunteer1 - 1:
      for card in rowCards:
        cardsVolunteer.add(card)
  rowVolunteer2 = int(f.readline())
  sameCards = 0
  guessedCard = -1
  for i in range(4):
    rowCards = f.readline().split()
    if i == rowVolunteer2 - 1:
      for card in rowCards:
        if card in cardsVolunteer:
          sameCards += 1
          guessedCard = card
  
  if sameCards == 0:
    print "Case #" + str(case) + ": Volunteer cheated!" 
  elif sameCards == 1:
    print "Case #" + str(case) + ": " + str(guessedCard)
  else:
    print "Case #" + str(case) + ": Bad magician!"
    