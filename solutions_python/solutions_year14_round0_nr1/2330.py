#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = input()
    
    for caseNr in xrange(1, testcases+1):
        answer = []
        row = []
        cards = []
        row1 = raw_input()     
        
        for i in range(4):
            cards.append(raw_input())
        
        row.append(cards[int(row1)-1])
        
        chosencards1 = row[0].split();
        
        cards = []
        row2 = raw_input()

        for i in range(4):
            cards.append(raw_input())
            
        row.append(cards[int(row2)-1])
        
        chosencards2 = row[1].split();
        
        for card in chosencards1:
            if card in chosencards2:
                answer.append(card)
        
        answers = len(answer)
        
        if answers == 0:
            print("Case #%i: Volunteer cheated!" % caseNr)
        elif answers >= 2:
            print("Case #%i: Bad magician!" % caseNr)
        else:
            print("Case #%i: %i" % (caseNr, int(answer[0])))