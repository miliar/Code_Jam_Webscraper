ERR_MAG = "Bad magician!"
ERR_VOL = "Volunteer cheated!"
import fileinput
NUM_OF_CASES = int(raw_input())
final_answer = []
def f(board1, board2, answer1, answer2):
    overlap = []
    for elem in board1[answer1-1]:
        if elem in board2[answer2-1]:
            overlap.append(elem)
    if len(overlap) == 0:
        return ERR_VOL
    elif len(overlap) == 1:
        return overlap[0]
    else:
        return ERR_MAG


for case in xrange(NUM_OF_CASES):
    answer1 = int(raw_input())
    board1, board2 = [], []
    for i in xrange(4):
        board1.append(map(int,raw_input().split()))
    answer2 = int(raw_input())
    for i in xrange(4):
        board2.append(map(int,raw_input().split()))
    final_answer.append(f(board1, board2, answer1, answer2))

for test_case in xrange(NUM_OF_CASES):
    answer = final_answer[test_case]
    if type(answer) == int:
        print "Case #%d: %d"%(test_case+1, answer)
    else:
        print "Case #%d: %s"%(test_case+1, answer)
