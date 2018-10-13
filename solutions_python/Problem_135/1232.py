#!/usr/bin/env python 

n = int(raw_input())

cards = [[], []]
answer = []

for case in range(n):
  for ii in range(2):
    answer.append(int(raw_input()))
    for row in range(4):
      cards[ii].append(raw_input().split())
  
  first_guess = cards[0][answer[0]-1]
  second_guess = cards[1][answer[1]-1]

  count = 0
  for card in first_guess:
    if card in second_guess:
      count += 1
      found = card

  if count > 1:
    print 'Case #' + str(case+1) + ': Bad magician!'

  if count == 1:
    print 'Case #' + str(case+1) + ': ' + found

  if count == 0:
    print 'Case #' + str(case+1) + ': Volunteer cheated!'

  #print first_guess
  #print second_guess
  #print 
  
  cards = [[], []]
  answer = [] 
