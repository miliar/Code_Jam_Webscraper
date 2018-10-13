import sys

def solution(answer1, cards1, answer2, cards2):
    firstline = cards1[answer1-1]
    secondline = cards2[answer2-1]
    answer = []
    for card in firstline:
        if card in secondline:
            answer.append(card)       
    if len(answer) == 0:
        return 'Volunteer cheated!'
     
    if len(answer) == 1:
        return str(answer[0])
    
    if len(answer) > 1:
        return 'Bad magician!'
      




numcases = int(sys.stdin.readline())
for casenum in range(1,numcases+1):
    answer1 = int(sys.stdin.readline().strip())
    cards1 = []
    card = []
    for i in range(0,4):
        line = sys.stdin.readline().strip().split()
        for num in line:
            card.append( ( int(num) ))
        cards1.append(card)
        card = []
    
    answer2 = int(sys.stdin.readline().strip())
    cards2 = []
    for i in range(0,4):
        line = sys.stdin.readline().strip().split()
        for num in line:
            card.append( ( int(num) ))
        cards2.append(card)
        card = []

    solution(answer1, cards1, answer2, cards2)
    print 'Case #' + repr(casenum) + ': ' + solution(answer1, cards1, answer2, cards2)