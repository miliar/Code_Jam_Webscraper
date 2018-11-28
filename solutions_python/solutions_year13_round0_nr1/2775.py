#!/usr/bin/python
def evaluate_candidate(candidate):
    winner = "Game has not completed"
    if '.' not in candidate:
        winner = "Draw"
        if 'O' not in candidate:
            winner = "X won"
        else:
            if 'X' not in candidate:
                winner = "O won"
    return winner

def generate_candidates(matrix):
    A = matrix[0][0] + matrix[1][0] + matrix[2][0] + matrix[3][0]
    B = matrix[0][1] + matrix[1][1] + matrix[2][1] + matrix[3][1]
    C = matrix[0][2] + matrix[1][2] + matrix[2][2] + matrix[3][2]
    D = matrix[0][3] + matrix[1][3] + matrix[2][3] + matrix[3][3]
    E = matrix[0][0] + matrix[0][1] + matrix[0][2] + matrix[0][3]
    F = matrix[1][0] + matrix[1][1] + matrix[1][2] + matrix[1][2]
    G = matrix[2][0] + matrix[2][1] + matrix[2][2] + matrix[2][3]
    H = matrix[3][0] + matrix[3][1] + matrix[3][2] + matrix[3][3]
    I = matrix[0][0] + matrix[1][1] + matrix[2][2] + matrix[3][3]
    J = matrix[0][3] + matrix[1][2] + matrix[2][1] + matrix[3][0]
    candidates = [A,B,C,D,E,F,G,H,I,J]
    return candidates

def process(matrix, case):
    candidates = generate_candidates(matrix)
    memory = "Blank"
    for i in range(10):
        answer = evaluate_candidate(candidates[i])
        #print answer, answer == "X won" or answer == "O won"
        if answer == "Game has not completed":
            memory = answer
        if answer == "X won" or answer == "O won":
            break
    if memory != "Blank" and answer == "Draw":
        print "Case #%i: %s" %(case, memory)
    else:
        print "Case #%i: %s" %(case, answer)

def input():
    T = int(raw_input())
    for i in range(1,T+1,1):
        row0 = raw_input()
        row1 = raw_input()
        row2 = raw_input()
        row3 = raw_input()
        if i is not T:
            new_line = raw_input()
        matrix = [row0,row1,row2,row3]
        process(matrix, i)

def main():
    input()
    # print evaluate_candidate('XXXX')
    # print evaluate_candidate('XXXT')
    # print evaluate_candidate('OOOO')
    # print evaluate_candidate('OOOT')
    # print evaluate_candidate('OO.O')
    # print evaluate_candidate('XXXO')

if __name__ == '__main__':
    main()