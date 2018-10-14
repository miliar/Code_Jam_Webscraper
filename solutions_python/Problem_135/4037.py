#!/usr/bin/python
import sys
fout = open('result.txt', 'a')
with open(sys.argv[1], 'r') as fin:
    lines = fin.readlines()
    T = int(lines[0].split()[0])
    #print T
    i = 0
    while i < T:
        base = 10*i
        first_ans = int(lines[base + 1].split()[0])
        first_cards = set([int(card) for card in lines[base + 2 + first_ans - 1].split()])
        second_ans = int(lines[base + 6].split()[0])
        second_cards = set([int(card) for card in lines[base + 7 + second_ans - 1].split()])
        card = first_cards.intersection(second_cards) 
        i += 1
        n = len(card)
        if n == 0:
            fout.write('Case #' + str(i) + ': Volunteer cheated!\n')
        elif n == 1:
            fout.write('Case #' + str(i) + ': ' + str(card.pop()) + '\n') 
        elif n > 1:
            fout.write('Case #' + str(i) + ': Bad magician!\n')
